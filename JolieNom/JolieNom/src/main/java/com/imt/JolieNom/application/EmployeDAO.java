package com.imt.JolieNom.application;

public class EmployeDAO {
    private int id;
    private String nom;

    public EmployeDAO(int id, String nom) {
        this.id = id;
        this.nom = nom;
    }

    public EmployeDAO() {
    }
    
    public int getId() {
        return id;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    
    public String getNom() {
        return nom;
    }
    
    public void setNom(String nom) {
        this.nom = nom;
    }
}
