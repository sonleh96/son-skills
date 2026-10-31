export const title = "Installer destination lifecycle";

const phases = {
  start: "Waiting to check",
  preflight: "Checking destinations",
  ready: "Ready to install",
  blocked: "Blocked by conflict",
  done: "Installed",
};

export const state = ({ phase, destinationWrites }) =>
  `${phases[phase]} - destination ${destinationWrites ? "changed" : "unchanged"}`;

export const step = (action, _from, to) =>
  ({
    Preflight: "check all destinations",
    EarlyWrite: "copy before checking",
    Resolve: to.phase === "blocked" ? "reject conflicting install" : "approve install",
    Write: "install approved files",
    Terminal: "stay installed",
  })[action];

export const group = ({ phase }) =>
  phase === "blocked" ? "Blocked" : phase === "done" ? "Done" : "In progress";

export const colors = {
  Blocked: "orange",
  Done: "teal",
  "In progress": "blue",
};
