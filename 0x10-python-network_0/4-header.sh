#!/bin/bash
# A script that sends a GET request, displays the body and,
# the header X-School-User_Id is sent with the value 98

curl -SH "X-School-User_Id: 98" "$1"
