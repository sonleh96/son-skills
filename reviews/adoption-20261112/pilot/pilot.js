(() => {
  const root = document.documentElement;
  const views = [...document.querySelectorAll('.view')];
  const viewStatus = document.querySelector('#view-status');
  const gestureStatus = document.querySelector('#gesture-status');
  const motionMode = document.querySelector('#motion-mode');
  const reducedButton = document.querySelector('#reduced-motion');
  const dragStage = document.querySelector('#drag-stage');
  const dragCard = document.querySelector('#drag-card');

  const pilot = {
    events: [],
    view: 0,
    drag: { x: 0, phase: 'idle', catches: 0 },
    record(type, detail = {}) {
      this.events.push({ type, at: performance.now(), ...detail });
      if (this.events.length > 100) this.events.shift();
      syncTelemetry();
    },
    state() {
      return {
        reducedMotion: reducedMotion(),
        view: this.view,
        drag: { ...this.drag },
        events: this.events.slice(),
      };
    },
  };
  window.__motionPilot = pilot;

  function reducedMotion() {
    return root.dataset.reducedMotion === 'true' || window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function syncTelemetry() {
    const recent = pilot.events.slice(-20).map((event) => ({
      type: event.type,
      at: Math.round(event.at),
    }));
    dragStage.dataset.pilotPhase = pilot.drag.phase;
    dragStage.dataset.pilotX = String(pilot.drag.x);
    dragStage.dataset.pilotCatches = String(pilot.drag.catches);
    dragStage.dataset.pilotReducedMotion = String(reducedMotion());
    dragStage.dataset.pilotEventTimestamps = pilot.events
      .slice(-20)
      .map((event) => `${event.type}:${Math.round(event.at)}`)
      .join(',');
    dragStage.dataset.pilotEvents = JSON.stringify(recent);
  }

  function setMode(reduced) {
    if (reduced) root.dataset.reducedMotion = 'true';
    else delete root.dataset.reducedMotion;
    reducedButton.setAttribute('aria-pressed', String(reduced));
    reducedButton.textContent = reduced ? 'Use full motion' : 'Use reduced motion';
    motionMode.textContent = `Motion mode: ${reduced ? 'reduced' : 'full'}`;
    pilot.record('motion-mode', { reduced });
  }

  reducedButton.addEventListener('click', () => {
    setMode(root.dataset.reducedMotion !== 'true');
  });

  function showView(nextIndex, direction) {
    const previousIndex = pilot.view;
    if (nextIndex === previousIndex) return;
    const previous = views[previousIndex];
    const next = views[nextIndex];
    previous.classList.remove('is-active', 'is-leaving-left', 'is-leaving-right');
    previous.classList.add(direction > 0 ? 'is-leaving-left' : 'is-leaving-right');
    next.classList.remove('is-leaving-left', 'is-leaving-right');
    next.setAttribute('aria-hidden', 'false');
    previous.setAttribute('aria-hidden', 'true');
    next.classList.add('is-active');
    pilot.view = nextIndex;
    viewStatus.textContent = `View ${nextIndex + 1} of ${views.length}`;
    pilot.record('view-change', { from: previousIndex, to: nextIndex, direction });
  }

  function step(direction) {
    const nextIndex = (pilot.view + direction + views.length) % views.length;
    showView(nextIndex, direction);
  }

  document.querySelector('#next').addEventListener('click', () => step(1));
  document.querySelector('#back').addEventListener('click', () => step(-1));

  let activePointer = null;
  let startX = 0;
  let startOffset = 0;
  let currentX = 0;
  let previousX = 0;
  let previousTime = 0;
  let velocity = 0;
  let settleToken = 0;

  function clamp(value, min, max) {
    return Math.min(Math.max(value, min), max);
  }

  function readRenderedX() {
    const transform = getComputedStyle(dragCard).transform;
    if (transform === 'none') return 0;
    const match = transform.match(/^matrix\(([^)]+)\)$/);
    if (match) return Number(match[1].split(',')[4]) || 0;
    const matrix3d = transform.match(/^matrix3d\(([^)]+)\)$/);
    if (matrix3d) return Number(matrix3d[1].split(',')[12]) || 0;
    return currentX;
  }

  function setDragX(value) {
    currentX = value;
    dragCard.style.setProperty('--drag-x', `${value}px`);
    pilot.drag.x = Math.round(value * 10) / 10;
    syncTelemetry();
  }

  function dragBounds() {
    const stageRect = dragStage.getBoundingClientRect();
    const cardRect = dragCard.getBoundingClientRect();
    const maxOffset = Math.max(0, (stageRect.width - cardRect.width) / 2);
    return { min: -maxOffset, max: maxOffset };
  }

  function clampDrag(value) {
    const bounds = dragBounds();
    return clamp(value, bounds.min, bounds.max);
  }

  function constrainDrag(reason = 'drag-resize') {
    const bounds = dragBounds();
    const before = currentX;
    const after = clamp(currentX, bounds.min, bounds.max);
    if (after !== before) setDragX(after);
    if (after !== before) pilot.record(reason, { before, after, min: bounds.min, max: bounds.max });
  }

  function startDrag(event) {
    if (activePointer !== null) return;
    activePointer = event.pointerId;
    settleToken += 1;
    const renderedX = clampDrag(readRenderedX());
    if (Math.abs(renderedX - currentX) > 1) {
      pilot.drag.catches += 1;
      pilot.record('drag-catch', { x: renderedX });
      gestureStatus.textContent = 'Caught during settle.';
    }
    setDragX(renderedX);
    startX = event.clientX;
    startOffset = renderedX;
    previousX = renderedX;
    previousTime = performance.now();
    velocity = 0;
    dragCard.classList.add('is-dragging');
    dragCard.setPointerCapture(event.pointerId);
    pilot.drag.phase = 'track';
    pilot.record('drag-start', { x: renderedX });
    gestureStatus.textContent = 'Tracking pointer.';
  }

  function moveDrag(event) {
    if (event.pointerId !== activePointer) return;
    const now = performance.now();
    const nextX = clampDrag(startOffset + event.clientX - startX);
    const elapsed = Math.max(now - previousTime, 1);
    velocity = (nextX - previousX) / elapsed;
    previousX = nextX;
    previousTime = now;
    setDragX(nextX);
  }

  function finishDrag(event) {
    if (event.pointerId !== activePointer) return;
    activePointer = null;
    if (dragCard.hasPointerCapture(event.pointerId)) dragCard.releasePointerCapture(event.pointerId);
    dragCard.classList.remove('is-dragging');
    const releaseX = currentX;
    const fast = Math.abs(velocity) > 0.8;
    const bounds = dragBounds();
    const far = Math.abs(releaseX) > Math.max(24, bounds.max * 0.55);
    const reduced = reducedMotion();
    const direction = Math.sign(releaseX || velocity);
    const target = reduced ? 0 : (fast || far ? (direction < 0 ? bounds.min : bounds.max) : 0);
    const token = ++settleToken;
    setDragX(target);
    pilot.drag.phase = 'release';
    pilot.record('drag-release', { from: releaseX, to: target, velocity, reduced });
    gestureStatus.textContent = `Released with ${Math.round(Math.abs(velocity) * 100) / 100}px/ms velocity.`;
    if (reduced) gestureStatus.textContent += ' Reduced motion settles without travel.';
    window.setTimeout(() => {
      if (token === settleToken && activePointer === null && Math.abs(currentX - target) < 1) {
        pilot.drag.phase = 'idle';
        syncTelemetry();
        gestureStatus.textContent = target === 0 ? 'Settled at center.' : 'Settled at the release point.';
      }
    }, reduced ? 20 : 240);
  }

  dragCard.addEventListener('pointerdown', startDrag);
  dragCard.addEventListener('pointermove', moveDrag);
  dragCard.addEventListener('pointerup', finishDrag);
  dragCard.addEventListener('pointercancel', finishDrag);
  window.addEventListener('resize', () => constrainDrag());

  document.querySelector('#reset-drag').addEventListener('click', () => {
    if (activePointer !== null) return;
    dragCard.classList.remove('is-dragging');
    setDragX(0);
    pilot.drag.phase = 'idle';
    pilot.record('drag-reset');
    gestureStatus.textContent = 'Idle.';
  });

  dragCard.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight') {
      event.preventDefault();
      setDragX(clampDrag(currentX + 24));
      gestureStatus.textContent = 'Keyboard moved right.';
    }
    if (event.key === 'ArrowLeft') {
      event.preventDefault();
      setDragX(clampDrag(currentX - 24));
      gestureStatus.textContent = 'Keyboard moved left.';
    }
  });

  window.matchMedia('(prefers-reduced-motion: reduce)').addEventListener?.('change', (event) => {
    motionMode.textContent = `Motion mode: ${event.matches ? 'reduced by system' : 'full'}`;
    pilot.record('system-motion-mode', { reduced: event.matches });
  });

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    motionMode.textContent = 'Motion mode: reduced by system';
  }

  constrainDrag();
  syncTelemetry();
})();
