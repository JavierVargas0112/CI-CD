package com.imt.JolieNom.presentation;

import java.util.List;


public class CreationEntrepriseDTO {
    private int id;
    private String nom;
    private List<Integer> idEmployes;

    public CreationEntrepriseDTO(){}
    public CreationEntrepriseDTO(int id, String nom, List<Integer> idEmployes) {
    this.id = id;
    this.nom = nom;
    this.idEmployes = idEmployes;
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
    public List<Integer> getIdEmployes() {
        return idEmployes;
    }
    public void setIdEmployes(List<Integer> idEmployes) {
    this.idEmployes = idEmployes;
    }
}