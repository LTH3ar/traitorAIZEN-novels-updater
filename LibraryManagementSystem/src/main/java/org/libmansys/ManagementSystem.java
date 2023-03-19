package org.libmansys;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;

import java.net.UnknownHostException;
import java.time.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.Path;


import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ManagementSystem {
    IOFuncs Lib1 = new IOFuncs();
    IOFuncs Lib2 = new IOFuncs();
    String filename1 = "novels.json";
    String filename2 = "novels_selected.json";


    // check connection
    public boolean checkConnection(String url) throws IOException {
        try {
            URL url1 = new URL(url);
            HttpURLConnection huc = (HttpURLConnection) url1.openConnection();
            huc.setRequestMethod("GET");
            huc.connect();
            int code = huc.getResponseCode();
            if (code != 200) {
                System.out.println("URL is not accessible");
                return false;
            }
        } catch (UnknownHostException e) {
            System.out.println("URL is not accessible");
            return false;
        }
        return true;
    }

    public void whateverList2File(List<String> lst, String filename){
        try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(filename, true)))) {
            for (String item_str : lst) {
                out.println(item_str);
            }
        } catch (IOException e) {
            System.out.println("Failed to write to file");
        }
    }


    // scrape list
    public void scrapeList() throws IOException {
        String url = "http://www.vn-meido.com/k1/index.php?topic=6646.msg38869#msg38869";

        //check connection
        if (!checkConnection(url)) {
            System.out.println("Connection failed");
            return;
        }
        //wait 1 second
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        Document doc = Jsoup.connect(url).get();
        Elements results = doc.select("a.bbc_link[href][target=_blank][rel=noopener]");
        int tmp_id = 0;
        int index = 0;
        // reset list
        if (Lib1.getNovels() != null) {
            Lib1.getNovels().clear();
        }
        for (Element result : results) {
            String tmp_url = result.attr("href");
            if (tmp_url.contains("topic=")) {
                String id = tmp_url.split("topic=")[1].split("&")[0];
                Novel novel = new Novel();
                novel.setIndex(index++);
                novel.setId(id);
                novel.setTitle(result.text());
                novel.setUrl(tmp_url);
                novel.setLastUpdate("N/A");
                Lib1.addNovel(novel);
            } else if (tmp_url.contains("msg=")){
                String id = tmp_url.split("msg=")[1].split("&")[0];
                Novel novel = new Novel();
                novel.setIndex(index++);
                novel.setId(id);
                novel.setTitle(result.text());
                novel.setUrl(tmp_url);
                novel.setLastUpdate("N/A");
                Lib1.addNovel(novel);
            } else {
                String id = "NoID_" + tmp_id++;
                Novel novel = new Novel();
                novel.setIndex(index++);
                novel.setId(id);
                novel.setTitle(result.text());
                novel.setUrl(tmp_url);
                novel.setLastUpdate("N/A");
                Lib1.addNovel(novel);
            }
        }
    }
    public void updateList() throws IOException {
        IOFuncs LibTmp = new IOFuncs();
        LibTmp.File2List(filename1);
        Lib1.clearList();
        scrapeList();
        for (Novel novel : Lib1.getNovels()) {
            for (Novel novelTmp : LibTmp.getNovels()) {
                if (novel.getId().equals(novelTmp.getId())) {
                    novel.setLastUpdate(novelTmp.getLastUpdate());
                }
            }
        }
        Lib1.List2File(filename1);
    }
    public void shortcutUpdateList() throws IOException {
        // check if filename1 exist
        File file = new File(filename1);
        if (file.exists()) {
            updateList();
        } else {
            scrapeList();
            Lib1.List2File(filename1);
        }
    }

    // Scrape last update time of all novels in the list
    IOFuncs LibTmp = new IOFuncs();
    public void scrapeLastUpdate(String url, String id) throws IOException {
        //check if url is accessible
        List<String> failed_list = new ArrayList<>();
        if (!checkConnection(url)) {
            System.out.println("Connection failed");
            System.out.println("Skipping " + id);
            failed_list.add(id);
            return;
        }
        //wait 1 second
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        Document page = Jsoup.connect(url).get();
        //span tag, smalltext modified floatright mvisible
        Elements results = page.select("span.smalltext.modified.floatright.mvisible");
        List<String> time_array = new ArrayList<>();
        for (Element result : results) {
            if (result.text().contains("by traitorAIZEN")) {
                time_array.add((result.text().split("by traitorAIZEN")[0].split(": ")[1]));
            } else if (results.isEmpty()) {
                time_array.add("N/A");
            }
        }
        if (time_array.isEmpty()) {
            time_array.add("N/A");
        }

        for (Novel novel : Lib1.getNovels()) {
            if (novel.getId().equals(id)) {
                if ((!novel.getLastUpdate().equals(time_array.toString())) && (!time_array.toString().equals("[N/A]"))) {
                    novel.setLastUpdate(time_array.toString());
                    LibTmp.addNovel(novel);
                } else{
                    System.out.println("\nNo change" + novel.getId());
                }
            }
        }

        // save failed list
        if (!failed_list.isEmpty()) {
            whateverList2File(failed_list, "failed_list.txt");
        }

    }
    public void scrapeAllLastUpdate() throws IOException {
        IOFuncs LibTmp2 = new IOFuncs();
        Lib1.File2List(filename1);
        Lib2.File2List(filename2);
        for (Novel novel : Lib1.getNovels()) {
            for (Novel novel2 : Lib2.getNovels()) {
                if (novel.getId().equals(novel2.getId())) {
                    scrapeLastUpdate(novel.getUrl(), novel.getId());
                    LibTmp2.addNovel(novel);
                    Lib1.List2File(filename1);
                    System.out.println(novel.getIndex()
                            + " " + novel.getId()
                            + " " + novel.getTitle()
                            + " " + novel.getUrl()
                            + " " + novel.getLastUpdate());
                }
            }
        }
        String filenameTmp = ("Update_"
                + DateTimeFormatter.ofPattern("dd-MM-yyyy_HH-mm-ss")
                .format(LocalDateTime.now()) + ".json");
        String filenameTmp2 = ("Update_Full_"
                + DateTimeFormatter.ofPattern("dd-MM-yyyy_HH-mm-ss")
                .format(LocalDateTime.now()) + ".json");
        LibTmp.List2File(filenameTmp);
        LibTmp2.List2File(filenameTmp2);
        Path presetPath = Paths.get(filenameTmp);
        Path presetPath2 = Paths.get(filenameTmp2);
        Path targetDir = Paths.get("output/update");

        try {
            // Check if the target directory exists, create it if not
            if (!Files.exists(targetDir)) {
                Files.createDirectories(targetDir);
            }

            // Move the preset file to the target directory
            Path targetFile = targetDir.resolve(presetPath.getFileName());
            Files.move(presetPath, targetFile);

            System.out.println("File moved successfully to " + targetFile);

            // Move the preset file to the target directory
            Path targetFile2 = targetDir.resolve(presetPath2.getFileName());
            Files.move(presetPath2, targetFile2);

            System.out.println("File moved successfully to " + targetFile2);
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }

    }
    public void shortcutScrapeLastUpdate() throws IOException{
        File file1 = new File(filename1);
        File file2 = new File(filename2);
        if (file1.exists() && file2.exists()) {
            scrapeAllLastUpdate();
        } else {
            //raise error
            System.out.println("Error: File not found");
        }
    }

    //print list
    public void printList(String filename) throws IOException {
        IOFuncs LibTmp = new IOFuncs();
        LibTmp.File2List(filename);
        for (Novel novel : LibTmp.getNovels()) {
            System.out.println("\n\nIndex: " + novel.getIndex()
                    + "\nID: " + novel.getId()
                    + "\nTitle: " + novel.getTitle()
                    + "\nURL: " + novel.getUrl()
                    + "\nLast_Update: " + novel.getLastUpdate());
        }
    }
    public void searchNovel(String filename, String inputStr) throws IOException {
        IOFuncs LibTmp = new IOFuncs();
        LibTmp.File2List(filename);
        //print what match the inputStr not case sensitive
        for (Novel novel : LibTmp.getNovels()) {
            if (novel.getTitle().toLowerCase().contains(inputStr.toLowerCase())) {
                System.out.println("\n\nIndex: " + novel.getIndex()
                        + "\nID: " + novel.getId()
                        + "\nTitle: " + novel.getTitle()
                        + "\nURL: " + novel.getUrl()
                        + "\nLast_Update: " + novel.getLastUpdate());
            }
        }
    }

    //Backup function
    public void backup(String filename){

        Path presetPath = Paths.get(filename);
        Path targetDir = Paths.get("output/backup");

        try {
            // Check if the target directory exists, create it if not
            if (!Files.exists(targetDir)) {
                Files.createDirectories(targetDir);
            }
            // check if the present file exists
            if (!Files.exists(presetPath)) {
                System.out.println("File not found");
            }

            // Move the preset file to the target directory
            Path targetFile = targetDir.resolve(presetPath.getFileName());
            Files.copy(presetPath, targetFile);
            Path filenameTmp = targetFile.resolveSibling(filename
                    + "__" + DateTimeFormatter
                    .ofPattern("dd-MM-yyyy_HH-mm-ss")
                    .format(LocalDateTime.now())
                    + ".json");
            Files.move(targetFile, filenameTmp);

            System.out.println("File backup successfully to " + filenameTmp);
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
    public void shortcutBackupAll(){
        backup(filename1);
        backup(filename2);
    }

    public void Menu() throws IOException {
        while (true) {
            Scanner input = new Scanner(System.in);
            System.out.println("Welcome to Novel Scraper");
            System.out.println("1. Scrape or update list of novels");
            System.out.println("2. Scrape last update time of all novels in the list");
            System.out.println("3. Print list of novels");
            System.out.println("4. Print list of selected novels");
            System.out.println("5. Search novel");
            System.out.println("6. Backup all files");
            System.out.println("7. Exit");
            System.out.print("Enter your choice: ");
            int choice = input.nextInt();
            switch (choice) {
                case 1 -> shortcutUpdateList();
                case 2 -> shortcutScrapeLastUpdate();
                case 3 -> printList(filename1);
                case 4 -> printList(filename2);
                case 5 -> {
                    System.out.print("Enter the title of the novel: ");
                    String inputStr = input.next();
                    searchNovel(filename1, inputStr);
                }
                case 6 -> shortcutBackupAll();
                case 7 -> System.exit(0);
                default -> System.out.println("Invalid choice");
            }
            //pause
            System.out.println("Press enter to continue...");
            input.nextLine();
            input.nextLine();

            //clear screen
            System.out.print("\033[H\033[2J");
            System.out.flush();
        }
    }
}