#!/usr/local/bin/expect
set user xxx
set passwd xxx

set timeout 20
spawn scp -r $user@spartan.hpc.unimelb.edu.au:/home/$user/assignment1/out/ out/
expect {
	"password:" { send "$passwd\r"}
}
interact
