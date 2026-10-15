# Specialist routing contract

The root agent routes actual work for the three data and machine learning specialists through the native `son-agent`.

This contract applies to direct skill invocations as well as skill selection made during Son mode.

At the root, dispatch a scoped native `son-agent` task with the full task context, the selected skill, the applicable playbook, owned files, and completion checks.

When the task is already running inside `son-agent`, load the selected skill and execute it directly.

Do not dispatch `son-agent` again, start a nested specialist route, or invoke a forked skill recursively.

If native delegation is unavailable, report that the route is unavailable and stop the specialist work.

Model selection and reasoning effort come from the central personal model policy and the active native controls.

The specialist skill supplies expertise and does not define a separate model role.

Use `data-scientist` for broad data research, exploratory analysis, statistical modeling, and general analytical recommendations.

Use `predictive-modeling` for predictive tabular modeling, feature engineering, model evaluation, and A/B experiment design.

Use `ml-engineer` for production training pipelines, serving, monitoring, and retraining.

Choose one concrete playbook and add specialist stages only when that playbook needs them.

Avoid a code or how-to explainer loop when the task asks for execution.
