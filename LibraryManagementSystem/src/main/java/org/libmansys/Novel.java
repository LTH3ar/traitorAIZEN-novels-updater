package org.libmansys;

public class Novel {
    private String id;
    private String title;
    private String url;
    private String last_update;

    //init
    public Novel() {
        this.id = "N/A";
        this.title = "N/A";
        this.url = "N/A";
        this.last_update = "N/A";
    }

    //getters
    public String getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getUrl() {
        return url;
    }

    public String getLast_update() {
        return last_update;
    }

    //setters
    public void setId(String id) {
        this.id = id;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public void setLast_update(String last_update) {
        this.last_update = last_update;
    }


}
