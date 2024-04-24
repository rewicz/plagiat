package pl.brakwic;

import java.util.*;

public class CosineSimilarity {

  // Metoda do tworzenia wektora BOW z listy słów
  public static Map<String, Integer> createBowVector(List<String> words) {
    Map<String, Integer> bow = new HashMap<>();

    String nameOfAlg = words.get(words.size() - 1);
    if(!Objects.equals(nameOfAlg, "*")){
      List<String> list = Arrays.asList(nameOfAlg.trim().split(" "));
      list.forEach(e -> bow.put(e,5));
      words.remove(nameOfAlg);
    }
    for (String word : words) {
      bow.put(word, bow.getOrDefault(word, 0) + 1);
    }
    return bow;
  }

  // Metoda do obliczania iloczynu skalarnego dwóch wektorów BOW
  public static double dotProduct(Map<String, Integer> vectorA, Map<String, Integer> vectorB) {
    double dotProduct = 0.0;
    for (String key : vectorA.keySet()) {
      if (vectorB.containsKey(key)) {
        dotProduct += vectorA.get(key) * vectorB.get(key);
      }
    }
    return dotProduct;
  }

  // Metoda do obliczenia normy wektora
  public static double vectorNorm(Map<String, Integer> vector) {
    double sum = 0.0;
    for (int value : vector.values()) {
      sum += value * value;
    }
    return Math.sqrt(sum);
  }

  // Metoda do obliczenia podobieństwa cosinusowego
  public static double cosineSimilarity(Map<String, Integer> vectorA, Map<String, Integer> vectorB) {
    return dotProduct(vectorA, vectorB) / (vectorNorm(vectorA) * vectorNorm(vectorB));
  }
}
