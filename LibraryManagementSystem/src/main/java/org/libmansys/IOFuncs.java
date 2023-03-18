package org.libmansys;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.io.FileReader;
//json lib
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.stream.JsonReader;

public class IOFuncs extends Novel {
    private List<Novel> novels;

    public IOFuncs() {
        novels = new ArrayList<>();
    }

    public void addNovel(Novel novel) {
        novels.add(novel);
    }

    public List<Novel> getNovels() {
        return novels;
    }

    public void setNovels(List<Novel> novels) {
        this.novels = novels;
    }

    public void clearList(){
        novels.clear();
    }

    //save list to json file
    public void List2File(String filename){
        Gson gson = new GsonBuilder().setPrettyPrinting().disableHtmlEscaping().create();
        try (FileWriter writer = new FileWriter(filename)) {
            gson.toJson(novels, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //load list from json file
    public void File2List(String filename){
        novels.clear();
        Gson gson = new Gson();
        if (novels != null){
            novels.clear();
        }
        //load json file
        try {
            JsonReader reader = new JsonReader(new FileReader(filename));
            Novel[] novelArray = gson.fromJson(reader, Novel[].class);
            novels.addAll(Arrays.asList(novelArray));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

}

