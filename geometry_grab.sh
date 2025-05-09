#!/bin/bash
# THIS SCRIPT EXTRACTS THE TIME AND NUCLEAR  
# POSITION PT-PT DATA FROM EHRENFEST DYNAMICS 
# LOG FILES GENERATED BY GAUSSIAN (GDV.I06P)
#
# WRITTEN BY: JOSEPH J. RADLER
# WRITTEN:  6/6/2017
# MODIFIED: 6/7/2017
#

# DEFINE THE CONDITION TO TEST
args="$#"

# CONDITIONAL TO PARSE THE NUMBER OF ARGUMENTS
# AND EXTRACT THE RAW DATA FROM THE .LOG FILE

if [ "$args" == "1" ]; then
	# GRAB THE DESIRED RAW ENERGY DATA
	`grep -A 1 'Summary for Ehrenfest Step' $1 > t_temp.txt`
	`grep -A 1 '105         78' $1 > coord_temp.txt`i
	
elif [ "$args" -gt "1" ]; then	
	while [ "$#" -gt "0" ]; do
		# CREATE TWO NEW TEMP FILES
		`touch t_temp.txt`
		`touch t_greptemp.txt`
		`touch coord_temp.txt`
		`touch coord_greptemp.txt`

		# GRAB THE DESIRED RAW ENERGY DATA
		`grep -A 1 'Summary for Ehrenfest Step' $1 > t_greptemp.txt`;
		`grep -A 1 '105         78' $1 > coord_greptemp.txt`;
		cat t_greptemp.txt >> t_temp.txt;
		cat coord_greptemp.txt >> coord_temp.txt;

		# TRASH COLLECTION
		rm t_greptemp.txt;
		rm coord_greptemp.txt;
		# SHIFT THE ARG REFERENCE DOWN ONE
		shift
	done
else echo "Error: Parser requires at least one input argument!"
fi

# MODIFY THE TIME AND COORDINATE FILES 
`grep -o '.\{0,12\}fs.\{0,0\}' t_temp.txt > t_only.txt`;
`awk '{print $1}' t_only.txt  > t_only2.txt`; 
# REMOVE SPURIOUS FIRST THREE LINES FROM DYNAMICS
`sed -e '1,3d' coord_temp.txt >> coord2_temp.txt`; 
`sed '/--/d' coord2_temp.txt > coord3_temp.txt`;
`awk '{print $4, $5, $6}' coord3_temp.txt > coord_only_temp.txt`;

# CALL PYTHON PARSER-CALCULATOR

`python distance_calc.py coord_only_temp.txt`

# PASTE OUTPUTS TOGETHER

`paste t_only2.txt distance.txt > distance_tseries.txt`

# FINAL TRASH-COLLECTION

`rm distance.txt`
`rm t_only.txt`
`rm t_only2.txt`
`rm coord_temp.txt`
`rm coord2_temp.txt`
`rm coord3_temp.txt`
`rm coord_only_temp.txt`
`rm t_temp.txt`



