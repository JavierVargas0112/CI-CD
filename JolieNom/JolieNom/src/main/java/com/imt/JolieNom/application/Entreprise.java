package com.imt.JolieNom.application;

import java.util.List;
import jakarta.persistence.*;
@Entity
public class Entreprise {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int id;
    private String nom;
    private List<Integer> idEmployes;

    public Entreprise(){}

    public Entreprise(int id, String nom, List<Integer> idEmployes) {
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