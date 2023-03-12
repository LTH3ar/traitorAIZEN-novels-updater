package org.libmansys;

import java.io.IOException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;



public class ManagementSystem {
    private ArrayList<Novel> novelsList;
    private ArrayList<Novel> novelsListSelected;
    private List<Novel> newUpdateList;
    private String listFile;
    private String listFileSelected;
    private String listFileNewUpdate;
    private String mainUrl;
    private MainFuncs mainFuncs;
    private ExtraFuncs extraFuncs;
    private Scanner input;

    public ManagementSystem() {
        novelsList = new ArrayList<>();
        novelsListSelected = new ArrayList<>();
        newUpdateList = new ArrayList<>();
        listFile = "novels_list.json";
        listFileSelected = "novels_list_selected.json";
        listFileNewUpdate = "new_update_list.json";
        mainUrl = "http://www.vn-meido.com/k1/index.php?topic=6646.msg38869#msg38869";
        mainFuncs = new MainFuncs(novelsList, novelsListSelected, newUpdateList);
        extraFuncs = new ExtraFuncs(novelsList, novelsListSelected);
        input = new Scanner(System.in);
    }

    public void optionList() throws IOException {
        while (true) {
            System.out.println("\n1. Scrape novels list(new) or update novels list(existing file)");
            System.out.println("2. scrape last update of novels (save to file)");
            System.out.println("3. add novel to selected list");
            System.out.println("4. remove novel from selected list");
            System.out.println("5. show selected list");
            System.out.println("6. save selected list to file");
            System.out.println("7. load selected list from file");
            System.out.println("8. show new update list");
            System.out.println("9. backup all");
            System.out.println("10. exit");

            System.out.print("Enter your choice: ");
            String choice = input.nextLine();

            if (choice.equals("1")) {
                if (mainFuncs.ifExist(listFile)) {
                    mainFuncs.updateNovelsList(mainUrl, listFile);
                } else {
                    mainFuncs.scrapeNovelsList(mainUrl);
                }
                mainFuncs.saveNovelsList(listFile);
            } else if (choice.equals("2")) {
                mainFuncs.scrapeNewUpdates();
            } else if (choice.equals("3")) {
                extraFuncs.novelSelectedAdd();
            } else if (choice.equals("4")) {
                extraFuncs.novelSelectedRemove();
            } else if (choice.equals("5")) {
                mainFuncs.printNovelsList();
            } else if (choice.equals("6")) {
                mainFuncs.exportSelectedNovels(listFileSelected);
            } else if (choice.equals("7")) {
                mainFuncs.importSelectedNovels(listFileSelected);
            } else if (choice.equals("8")) {
                mainFuncs.printNewUpdates();
                mainFuncs.exportNewUpdates();
            } else if (choice.equals("9")) {
                extraFuncs.backupNovelsList();
            } else if (choice.equals("10")) {
                System.exit(0);
            } else {
                System.out.println("Invalid choice");
            }
        }
    }
}
