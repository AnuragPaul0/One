
public class TestImpl implements TestIfc {

	public boolean isReverseNumber(int number) { int t, r, s = 0; t = number;
	while(number>0){ r = number%10; s = s*10+r; number/=10;
	if(t == s){
	return true;}
	else{
	return false;}}}}

public class TestImpl  { public String longest(String[] wordList){
    int c = wordList[0].length(); String re = "";
	for(int i = 1;i<wordList.length;i++) { if c < wordList[i].length() {
	    c = wordList[i].length(); re = wordList[i];
	} if c == wordList[i].length() { re = "null";}} return re;
}}


import java.utils.Arrays;
public class TestImpl implements TestIfc {

	public int findMissingNumber(int[] arr){
Arrays.sort(arr); for(int n = 1; n < arr.length; n++) {
    if (arr[n]-arr[n-1]!=1) {
        return arr[n]-1;
    }
}
	}
	
}
