package com.imt.JolieNom.application;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.imt.JolieNom.infrastructure.EntrepriseRepository;

import jakarta.ws.rs.client.Client;
import jakarta.ws.rs.client.ClientBuilder;
import jakarta.ws.rs.client.WebTarget;
import jakarta.ws.rs.core.GenericType;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

//permet à Spring d'initialiser cet objet et de le configurer
@Service
public class EntrepriseService {
    //permet de récupérer l'instance de EntrepriseRepository dans Spring et demanipuler JPA à travers cette dernière
    @Autowired
    private EntrepriseRepository repo;

    public List<Entreprise> getEntreprise(){
        return repo.findAll();//retourne toutes les entreprises contenues en bdd
    }

    public void creationEntreprise(Entreprise entreprise){
    repo.save(entreprise);
    }

    public List<EmployeDAO> getEmployes(List<Integer> idEmployes){
        //déclaration de l'objet permettant de déclencher un appel REST
        Client client = ClientBuilder.newClient();
        //on paramètre le lien d'appel, notre module Employe
        WebTarget target = client.target("http://localhost:8081/api/employes");
        // Ajout des query params représentant les identifiants d'employés
        for (Integer id : idEmployes) {
            target = target.queryParam("idEmployes", id);
        }
        Response response = target.request(MediaType.APPLICATION_JSON).get();
        //ici, cela nous permet de convertir directement la réponse du webservice en objet EmployeDAO
        List<EmployeDAO> employes = response.readEntity(new GenericType<List<EmployeDAO>>() {});
        response.close();
        client.close();
        return employes;
    }
}