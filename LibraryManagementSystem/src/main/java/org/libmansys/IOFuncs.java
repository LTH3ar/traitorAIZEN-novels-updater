package org.libmansys;
import java.util.ArrayList;
import java.util.List;

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

}

