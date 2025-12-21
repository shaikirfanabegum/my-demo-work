package main

deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  sc := container.securityContext
  not sc
  msg := sprintf("DENY: %s/%s container '%s' missing securityContext", [input.kind, input.metadata.name, container.name])
}

deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  sc := container.securityContext
  sc.allowPrivilegeEscalation == true
  msg := sprintf("DENY: %s/%s container '%s' allowPrivilegeEscalation must be false", [input.kind, input.metadata.name, container.name])
}

deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  sc := container.securityContext
  not sc.capabilities.drop
  msg := sprintf("DENY: %s/%s container '%s' must drop Linux capabilities", [input.kind, input.metadata.name, container.name])
}
