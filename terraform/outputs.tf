output "account_id" {
  value = data.aws_caller_identity.current.account_id
}

output "user_id" {
  value = data.aws_caller_identity.current.user_id
}

output "region" {
  value = data.aws_region.current.name
}

output "instance_ip_addr" {
  value = aws_instance.web.private_ip
}

output "subnet_id" {
  value = aws_instance.web.subnet_id
}