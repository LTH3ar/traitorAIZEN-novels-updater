package org.libmansys;

import java.io.IOException;

//just run ManagementSystem.java
public class Main {
    public static void main(String[] args) throws IOException {
        ManagementSystem ms = new ManagementSystem();
        //ms.scrapeList();
        //ms.saveList2File();
        ms.File2List();
        ms.printList();
    }
}