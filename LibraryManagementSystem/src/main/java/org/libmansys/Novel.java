package org.libmansys;
public class Novel {
    private String index = "N/A";
    private String id = "N/A";
    private String title = "N/A";
    private String url = "N/A";
    private String lastUpdate = "N/A";

    public String getIndex() {
        return index;
    }

    public void setIndex(int index) throws IllegalArgumentException {
        if (index >= 0) {
            this.index = String.valueOf(index);
        } else {
            throw new IllegalArgumentException("Invalid index");
        }
    }

    public String getId() {
        return id;
    }

    public void setId(String novelId) throws IllegalArgumentException {
        if (novelId != null && !novelId.isEmpty()) {
            this.id = novelId;
        } else {
            this.id = "N/A";
        }
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String novelTitle) throws IllegalArgumentException {
        if (novelTitle != null && !novelTitle.isEmpty()) {
            this.title = novelTitle;
        } else {
            this.title = "N/A";
        }
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String novelUrl) throws IllegalArgumentException {
        if (novelUrl != null && !novelUrl.isEmpty()) {
            this.url = novelUrl;
        } else {
            this.url = "N/A";
        }
    }

    public String getLastUpdate() {
        return lastUpdate;
    }

    public void setLastUpdate(String lastUpdate) throws IllegalArgumentException {
        if (lastUpdate != null && !lastUpdate.isEmpty()) {
            this.lastUpdate = lastUpdate;
        } else {
            this.lastUpdate = "N/A";
        }
    }
}
