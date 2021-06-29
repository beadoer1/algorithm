// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

class Solution1 {

    public static void main(String[] args) {
        solution("John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker", "Example");
    }

    public static String solution(String S, String C) {

        String lowerCaseS = S.toLowerCase(Locale.ROOT);
        String lowerCaseAndDelHyphens = lowerCaseS.replaceAll("-", "");
        String[] nameList = lowerCaseAndDelHyphens.split("; ");
        String company = C.toLowerCase(Locale.ROOT);

        List<String> emailList = new ArrayList<>();
        for (String name : nameList) {
            String[] nameSplitParts = name.split(" ");
            String firstName = nameSplitParts[0];
            String lastName = nameSplitParts[nameSplitParts.length - 1];
            if (lastName.length() > 8) {
                lastName = lastName.substring(0,8);
            }

            int num = 1;
            String email;
            do{
                if (num == 1) {
                    email = firstName + "." + lastName + "@" + company + ".com";
                } else {
                    email = firstName + "." + lastName + num + "@" + company + ".com";
                }
                num++;
            } while(emailList.contains(email));
            emailList.add(email);
        }

        String emailListAsString = String.join("; ", emailList);

        return emailListAsString;
    }
}
