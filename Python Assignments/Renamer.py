LorR = 'L'
Apndg = 'Leg'
Type = 'Geo'

import maya.cmds as mc
def renamer(lorR, apndg, number, type):

       sel = mc.ls(sl = True)
       for i in range(len(sel)):
              mc.rename(sel[i], lorR + "_" + apndg + "_" + str(i) + "_" + type)

renamer(LorR, Apndg, Number, Type)





'''
    //Variables
	string $name = "L_Leg_###_Geo";
	string $tokens[];
	string $selection[];
	
	//Tokenizes the name, and puts the selection into a variable
	tokenize $name "#" $tokens;
	$selection = `ls -sl`;
	
	//Incorrect naming input
	if (size($tokens) != 2){
		error("Input string is not in the correct form. Use \"Prefix_##_Suffix\"");
	}
	
	//Missing Selection Warning
	if (!size($selection) > 0){
            error ("Missing selection");
    }
	
	//Subtracts number characters from naming characters 
	int $numberDelim = size($name) - size($tokens[0]) - size($tokens[1]);
	
	//This loops through the selection and subtracts delimiter from iterator  
	for($i=0; $i<size($selection); $i++){
		int $digitsIter = `size((string)($i+1))`;
		int $paddingNum = $numberDelim - $digitsIter;
		string $pad = "";
		
		//This adds zeroes to the name
		for ($j=0; $j<$paddingNum; $j++){
			$pad = $pad + "0"; 
		}
		
		//This concats all the work into one variable, then renames the selection to the new name		
		string $newName = $tokens[0] + $pad + ($i + 1) + $tokens[1];
		rename $selection[$i] $newName;
'''