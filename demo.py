{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "lambda:CreateFunction",
                "lambda:UpdateFunctionCode",
                "iam:PassRole",
                "lambda:GetFunction",
                "lambda:UpdateFunctionConfiguration"
            ],
            "Resource": [
                "arn:aws:iam::539088561624:role/jenkinsdemo-role-os99b3fk",
                "arn:aws:lambda:us-east-1:539088561624:function:jenkinsdemo"
            ]
        }
    ]
}
