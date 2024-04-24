package pl.brakwic;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class UtilWord {
  static List<String> prepareWords(String basis) {
    String sentence = basis;
    sentence = sentence.toUpperCase();

    // extract name of algorithm
    String nameOfAlgorithm = extractTextInBrackets(sentence);
    if(nameOfAlgorithm != null) {
      sentence = sentence.replace(nameOfAlgorithm, "");
    }

    sentence = removePunctuation(sentence);
    sentence = removeMeaninglessWords(sentence);

    List<String> words = new ArrayList<>(Arrays.asList(sentence.trim().split(" ")));
    words.add(nameOfAlgorithm);
    return words;
  }

  public static String extractTextInBrackets(String inputString) {
    Pattern pattern = Pattern.compile("\\[(.*?)\\]");
    Matcher matcher = pattern.matcher(inputString);

    if (matcher.find()) {
      return matcher.group(1);
    } else {
      return "*";
    }
  }

  public static String removePunctuation(String inputString) {
    Pattern pattern = Pattern.compile("\\p{Punct}+");
    Matcher matcher = pattern.matcher(inputString);
    return matcher.replaceAll("");
  }

  public static String removeMeaninglessWords(String input) {
    List<String> meaninglessWords = Arrays.asList("A", "AN", "THE", "IN", "ON", "AT", "AND", "OR", "OF", "BY", "THIS", "THAT", "THESE" , "THOSE", "TOO" , "THEIR", "IF", "IS", "ARE" , "TO", "IT", "ITS", "THEIR", "ALGORITHM");
    String regexPattern = "\\b(" + String.join("|", meaninglessWords) + ")\\b";
    String cleanedText = input.replaceAll(regexPattern, "");
    cleanedText = cleanedText.trim().replaceAll("\\s+", " ");

    return cleanedText;
  }
}
