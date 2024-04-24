package pl.brakwic;

import java.io.InputStream;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Printer {

  // Metoda do tworzenia wektora BOW z listy słów
  public static void print(Map<String, Double> map) {

    Map<String, Double> sortedMap = map.entrySet().stream()
        .sorted(Map.Entry.<String, Double>comparingByValue().reversed())
        .collect(Collectors.toMap(
            Map.Entry::getKey,
            Map.Entry::getValue,
            (oldValue, newValue) -> oldValue, LinkedHashMap::new));

    String filename = "data.txt";

    HashMap<String, String> algorithmsCodeMap = new HashMap<>();
    loadAlgorithms(filename, algorithmsCodeMap);


    if(sortedMap.isEmpty()) {
      System.out.println("Nie wykryto podobieństwa w załączonym algorytmie.");

    }
    for (Map.Entry<String, Double> entry : sortedMap.entrySet()) {
      String algKey = entry.getKey();
      Double algValue = entry.getValue();

      // Wyświetl wartość dla algorytmu
      System.out.println("Załączony algorytm jest podobny do algorymu z pliku " + algKey + " w " + Math.round(algValue * 100) + "%");

      // Znajdź kod dla algorytmu i go wyświetl
        System.out.println();
        System.out.println(algorithmsCodeMap.get(algKey));
        System.out.println();
        System.out.println();


    }
  }

  private static void loadAlgorithms(String filePath, HashMap<String, String> algorithmsCodeMap) {
    InputStream inputStream = Main.class.getClassLoader().getResourceAsStream(filePath);
    if (inputStream == null) {
      System.out.println("Nie można znaleźć pliku " + filePath);
      return;
    }
    try (Scanner scanner = new Scanner(inputStream)) {
      boolean isRecording = false;
      String currentAlgKey = "";
      StringBuilder currentAlgCode = new StringBuilder();

      while (scanner.hasNextLine()) {
        String line = scanner.nextLine();
        if (line.startsWith("alg")) {
          isRecording = true;
          currentAlgKey = line.trim();
          currentAlgCode = new StringBuilder();
        } else if (line.startsWith("#")) {
          if (isRecording && currentAlgKey.length() > 0) {
            algorithmsCodeMap.put(currentAlgKey, currentAlgCode.toString());
            isRecording = false;
            currentAlgKey = "";
          }
        } else if (isRecording) {
          currentAlgCode.append(line).append("\n");
        }
      }
    }
  }
}
