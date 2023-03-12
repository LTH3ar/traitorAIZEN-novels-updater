package org.libmansys;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

import com.google.gson.Gson;

public class Input {
    private List<Novel> novelsList;
    private List<Novel> novelsListSelected;

    public Input(List<Novel> novelsList, List<Novel> novelsListSelected) {
        this.novelsList = novelsList;
        this.novelsListSelected = novelsListSelected;
    }

    // novels_list
    public void inputNovel(int index, String novelId, String novelTitle, String novelUrl, String lastUpdate, List<Novel> lst) {
        Novel novel = new Novel();
        try {
            novel.setIndex(index);
            novel.setId(novelId);
            novel.setTitle(novelTitle);
            novel.setUrl(novelUrl);
            novel.setLastUpdate(lastUpdate);
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
            return;
        }
        lst.add(novel);
    }

    public void loadNovelsList(String fileName, List<Novel> lst) {
        Gson gson = new Gson();
        try (FileReader reader = new FileReader(fileName)) {
            Novel[] novels = gson.fromJson(reader, Novel[].class);
            for (Novel novel : novels) {
                inputNovel(Integer.parseInt(novel.getIndex()), novel.getId(), novel.getTitle(), novel.getUrl(), novel.getLastUpdate(), lst);
            }
        } catch (IOException e) {
            System.err.println("Error reading from file: " + e.getMessage());
        }
    }
}
