package org.libmansys;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;


import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ManagementSystem {
    IOFuncs Lib1 = new IOFuncs();
    IOFuncs Lib2 = new IOFuncs();
    public void scrapeList() throws IOException {
        String url = "http://www.vn-meido.com/k1/index.php?topic=6646.msg38869#msg38869";
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
    //print list
    public void printList() {
        for (Novel novel : Lib1.getNovels()) {
            System.out.println(novel.getIndex() + " " + novel.getId() + " " + novel.getTitle() + " " + novel.getUrl() + " " + novel.getLastUpdate());
        }
    }

    //save list to json file
    String filename = "novels.json";
    public void saveList2File() {
        Lib1.saveList2File(filename);
    }
    public void File2List() {
        Lib1.File2List(filename);
    }
}
