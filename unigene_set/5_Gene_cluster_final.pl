#!/usr/bin/perl
# Programming for  Clustering
# Written by  Prusoth
# unit testing has to be done.

use strict;
no strict qw(refs);
use Data::Dumper;
use Storable;

open(FILE, 'T_mapped_regions.txt');

my $hash;
my $cr_hash;
my $count = 0;
while(my $line = <FILE>)
{
	my @data = split(/\s/, $line);
	$hash->{$count} = {
				'g_id' => $data[0],
				'chro_id' => $data[1],
				'start' => int($data[2]),
				'end' => int($data[3]),
				'unknown' => $data[4],
				};	
	$count++;

	$cr_hash->{$data[1]} = [] unless(exists $cr_hash->{$data[1]});
	my $cr_arr = {
				'g_id' => $data[0],
				'chro_id' => $data[1],
				'start' => int($data[2]),
				'end' => int($data[3]),
				'unknown' => $data[4],
		};
	push($cr_hash->{$data[1]}, $cr_arr);	
}
#print Dumper($cr_hash);
print scalar(keys %$hash);
close FILE;
print "Create a file final_updated_cluster.txt";
<>;
open(FILE2, '>final_updated_cluster.txt');
print FILE2 "CLuster\tg_id\tchro_id\tstart\tend\tunknown\n";
my $cluster = 1;
my $sec_hash = $hash;
my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime();
printf("Time Format - HH:MM:SS\n");
printf("%02d:%02d:%02d", $hour, $min, $sec);
my $cr_hash2 = $cr_hash;
foreach my $chro (keys %$cr_hash)
{	
	my @sorted = sort { $a->{start} <=> $b->{start}} @{$cr_hash->{$chro}};
	my @in_arr = @sorted;
	my @out_arr = @sorted;	
	for(my $i =0; $i < scalar @out_arr;$i++)
	{
		my $chro_1 = $out_arr[$i];
		my $count = 0;
		next unless(defined $chro_1->{g_id} );
		print FILE2 "$cluster\t$chro_1->{g_id}\t$chro_1->{chro_id}\t$chro_1->{start}\t$chro_1->{end}\t$chro_1->{unknown}\n";
		delete $in_arr[$i];
		my $start = $chro_1->{start};
		my $end =  $chro_1->{end};		
		my $except_arr = [];  
		for (my $j = 0; $j < scalar @in_arr; $j++)
		{
			my $chro_2 = $in_arr[$j];
			
			if(int($chro_2->{start}) < int($end) && int($chro_2->{end}) > int($start))
			{
				$start = $chro_2->{start} if($chro_2->{start} < $start);
				$end = 	$chro_2->{end} if($chro_2->{end} > $end);
				print FILE2 "$cluster\t$chro_2->{g_id}\t$chro_2->{chro_id}\t$chro_2->{start}\t$chro_2->{end}\t$chro_2->{unknown}\n";
				$count++;
				delete $in_arr[$j];
				delete $out_arr[$j];
			}
			else { $in_arr[$j]->{'index'} = $j ;push(@$except_arr,$in_arr[$j]);}	
		}
		for(my $k = 0; $k < scalar @$except_arr; $k++)
		{
			my $except_chro = $except_arr->[$k];
			if(int($except_chro->{start}) < int($end) && int($except_chro->{end}) > int($start))
			{
				print FILE2 "$cluster\t$except_chro->{g_id}\t$except_chro->{chro_id}\t$except_chro->{start}\t$except_chro->{end}\t$except_chro->{unknown}";
				$count++;
				print "$start $end\n" if($except_chro->{g_id} eq 'asmbl_261449');
				delete $except_arr->[$k];
				delete $out_arr[$except_chro->{'index'}];

			}
			print "$start $end second\n" if($except_chro->{g_id} eq 'asmbl_261449');
		}		
		delete $out_arr[$i];
		$cluster++; 	
	}
}
exit;

foreach my $key1 (sort {$a <=> $b} keys %$hash)
{
	# print "$key1";	
	# print Dumper($hash->{$key1});
	next if(! $hash->{$key1}{start} or ! $hash->{$key1}{end}); 
	print FILE2 "$cluster\t$hash->{$key1}{g_id}\t$hash->{$key1}{chro_id}\t$hash->{$key1}{start}\t$hash->{$key1}{end}\t$hash->{$key1}{unknown}";
	# print "$cluster\t$hash->{$key1}{g_id}\t$hash->{$key1}{chro_id}\t$hash->{$key1}{start}\t$hash->{$key1}{end}\t$hash->{$key1}{unknown}";
	my $start = $hash->{$key1}{start};
	my $end = $hash->{$key1}{end};
	my $chro = $hash->{$key1}{chro_id};
	my $count = 0;
	delete $sec_hash->{$key1};
	foreach my $key2 (sort {$a <=> $b} keys %$sec_hash)
	{
		#print "$key2\t$sec_hash->{$key2}{start}\t$sec_hash->{$key2}{end}\n ";
		next if($sec_hash->{$key2}{chro_id} ne $chro);
		#next if($hash->{$key1}{start} == $sec_hash->{$key2}{start} && $hash->{$key1}{end} == $sec_hash->{$key2}{end} && $hash->{$key1}{unknown} == $sec_hash->{$key2}{unknown});	
		if(int($sec_hash->{$key2}{start}) < int($end) && int($sec_hash->{$key2}{end}) > int($start) && $sec_hash->{$key2}{chro_id} eq $chro)
		{
			$start = $sec_hash->{$key2}{start} if($start > $sec_hash->{$key2}{start}); 
			$end = $sec_hash->{$key2}{end} if($end < $sec_hash->{$key2}{end}); 
			print "$sec_hash->{$key2}{g_id} $start $end \n";
			print FILE2 "$cluster\t$sec_hash->{$key2}{g_id}\t$sec_hash->{$key2}{chro_id}\t$sec_hash->{$key2}{start}\t$sec_hash->{$key2}{end}\t$sec_hash->{$key2}{unknown}";
			#print "$cluster\t$sec_hash->{$key2}{g_id}\t$sec_hash->{$key2}{chro_id}\t$sec_hash->{$key2}{start}\t$sec_hash->{$key2}{end}\t$sec_hash->{$key2}{unknown}";

			
			delete $hash->{$key2};
			delete $sec_hash->{$key2};
			$count++;			
		}		

	}
	delete $hash->{$key1};

	#print "First Hash : ".scalar(keys %$hash)."\n";
	#print "Second Hash :". scalar(keys %$sec_hash)."\n\n";
	last if(scalar(keys %$sec_hash) == 0 or scalar(keys %$hash) == 0);
	$cluster++;
}
my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime();
printf("Time Format - HH:MM:SS\n");
printf("%02d:%02d:%02d", $hour, $min, $sec);
