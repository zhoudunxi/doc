#!/usr/bin/perl
use utf8;
my @lines;
system('ps -ef |awk \'/pt-kill/{system("kill -9 " $2)}\'');
#kzwawa master
$lines[0] =  "rm-uf674qnrl41677g0s.mysql.rds.aliyuncs.com kzww DYycEQiyUzet\@r20 12";
#kzwawa topic
$lines[1] =  "rm-uf614u42y571yq463.mysql.rds.aliyuncs.com kzww DYycEQiyUzet\@r20 12";
#kzwawa slave01
$lines[2] =  "rr-uf64sbpu3wg5362j7.mysql.rds.aliyuncs.com wawa am\#&PF\$Azhf9C\$9O 12";
#kzwawa slave02
$lines[3] =  "rr-uf6d7865a1x624mv6.mysql.rds.aliyuncs.com wawa am\#&PF\$Azhf9C\$9O 12";
#kzwawa slave03
$lines[4] =  "rr-uf6n4l3cwls87sqqo.mysql.rds.aliyuncs.com wawa am\#&PF\$Azhf9C\$9O 12";
#topic slave01
$lines[5] =  "rr-uf6z6f68l0vxb2661.mysql.rds.aliyuncs.com wawa am\#&PF\$Azhf9C\$9O 12";

foreach (@lines) {
    chomp;
    my @fields = split(/\s+/);
    my $time;
    if(scalar(@fields) >= 3) {
        my $logfile = (split(/\./, $fields[0]))[0];
        my $cmd;
        $time = $fields[3]; 
        if ( $time < 1 ) {
            $time = 30;
        }

        if( $fields[0] =~  /^rr/ ) {
            $cmd = "kill-query";
        } else {
            $cmd = "kill-query";
        }

        system("pt-kill",
            "--host", $fields[0],
            "--user", $fields[1],
            "--password", $fields[2],
            "--no-version-check",
            "--victims", "all",
            "--busy-time", $time,
            "--interval", 5,
            "--$cmd",
            "--print",
            "--log", "/tmp/${logfile}.log",
            "--daemonize")
    }
}
