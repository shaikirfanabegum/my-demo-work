package main

deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  not container.resources.requests
  msg := sprintf("DENY: %s/%s container '%s' missing resources.requests", [input.kind, input.metadata.name, container.name])
}

deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  not container.resources.limits
  msg := sprintf("DENY: %s/%s container '%s' missing resources.limits", [input.kind, input.metadata.name, container.name])
}

deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  not container.readinessProbe
  msg := sprintf("DENY: %s/%s container '%s' missing readinessProbe", [input.kind, input.metadata.name, container.name])
}

deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  not container.livenessProbe
  msg := sprintf("DENY: %s/%s container '%s' missing livenessProbe", [input.kind, input.metadata.name, container.name])
}
