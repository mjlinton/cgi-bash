#!/bin/bash
#
# To encode the binary file, run this command in the directory where it's lacated.
# 	$ compress < binary | uuencode -m binary.Z
#
function form_decoder { echo -n "${1}" | sed 's/^/[/ ; s/=/]="/g ; s/\&/" [/g ; s/$/"/ ; s/+/ /g ; s/%/\\\\x/g' | xargs -0 printf '%b' ; }
function form_key     { echo -n "${1}" | sed 's/^/"/ ; s/=[^&]*&/" "/g ; s/=.*$/"/' ; }

case ${PATH_INFO} in 
/favicon.ico) echo -ne "Content-Type: image/x-icon\n\n" ; /usr/bin/uudecode -o /dev/stdout << EOF 2>/dev/null | /bin/zcat
begin-base64 644 favicon.ico.Z
H52QAAAEEAgAgsGACFEMBGAhIUIICEEgHEgAocWLFyFijBOHEIB8IAGsGwkgVKhRAJo0oQLg2bNmAgM4ivkKIbaYYgAoUJACoTKEzC7+G3rRnVGjHo4qraH0
aAsfSsNBG0eKiDsRRquUa9VtSrRyRAAQ4NoqCo1Ld+7YaaUNxh5czJgh06ONDbJFu/ImO4XsUBpeu5gl4nVIUzbAt9TgypUKzTJcarqlyoSLUeBO3bpt02WJ
2SGu3bLZ2mPLVjdtp/Es06SpWyuMsGPLnk27NgA=
===
EOF
;;
/logo.png) echo -ne "Content-Type: image/png\n\n" ; /usr/bin/uudecode -o /dev/stdout << EOF 2>/dev/null | /bin/zcat
begin-base64 644 logo.png.Z
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
cAASUAgbsAf9sAM1gA8QAQBJUAROQASuIARgIAg=
====
EOF
;;
*)
[ "${REQUEST_METHOD}" = "POST" ] && read QUERY_STRING ;
[ -z ${QUERY_STRING} ] || eval $(echo -n "declare -A FORM=($(form_decoder ${QUERY_STRING})) ; FORM_KEY=($(form_key ${QUERY_STRING}))") ;
echo -ne "Content-Type: text/html\n\n"\
"<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.1//EN\" \"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd\">\n"\
"<html><head>\n"\
"<title>Environment</title>\n"\
"<link rel=\"icon\" href=\"http://${SERVER_NAME}${SCRIPT_NAME}/favicon.ico\">\n"\
"<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\"></head>\n"\
"<body><img src=\"http://${SERVER_NAME}${SCRIPT_NAME}/logo.png\"><h1>Environment</h1>\n"\
"<pre>$(/bin/env)</pre>\n"\
"$([ -z ${QUERY_STRING} ] || echo -n "<pre>FORM_KEY=($(form_decoder ${QUERY_STRING})</pre>" ; )"\
"$([ ${#FORM[@]} -gt 0 ] && echo -n "<pre>$(for KEY in ${FORM_KEY[@]} ; do echo "\$FORM[${KEY}]=\"${FORM[$KEY]}\"" ; done)</pre>" ; )"\
"<h3>Form::Get</h3>\n<form method=get>"\
"First Nname:<input type=\"text\" name=\"firstname\">"\
"<br>Last Name:<input type=\"text\" name=\"lastname\">"\
"<br>Birth Date:<input type=\"text\" name=\"dob\">"\
"<br><input type=\"submit\"></form>"\
"<h3>Form::Post</h3>\n""<form method=post>"\
"First Nname:<input type=\"text\" name=\"firstname\">"\
"<br>Last Name:<input type=\"text\" name=\"lastname\">"\
"<br>Birth Date:<input type=\"text\" name=\"dob\">"\
"<br><input type=\"submit\"></form>"\
"</body></html>" ;;
esac

exit 0 ;
