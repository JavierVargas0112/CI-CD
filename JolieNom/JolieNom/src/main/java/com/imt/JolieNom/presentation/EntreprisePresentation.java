package com.imt.JolieNom.presentation;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;

import com.imt.JolieNom.application.Entreprise;
import com.imt.JolieNom.application.EntrepriseService;
import com.imt.JolieNom.application.EmployeDAO;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;

@Path("entreprises")
public class EntreprisePresentation {

    @Autowired
    private EntrepriseService service;

    @GET
    @Produces("application/json")
    public List<EntrepriseDTO> getEntreprises(){
        //ne pas oublier de mapper les données :)
        EntrepriseMapper em = new EntrepriseMapper();
        //on récupère toutes les entreprises
        List<Entreprise> entreprisesBdd = service.getEntreprise
        ();
        //cette liste nous sert d'objet de retour
        List<EntrepriseDTO> entreprisesRetournees = new ArrayList<>();
        //dans cette partie, on transforme les données en EntrepriseDTO
        for(Entreprise e : entreprisesBdd){
            EntrepriseDTO entrepriseAAjouter = new EntrepriseDTO();
            entrepriseAAjouter = em.mapEntrepriseToEntrepriseDTO(e);
            //partie Employes, on va interroger le module Employe
            //et mettre à dispo les infos employés dans chaque entreprise
            if(!e.getIdEmployes().isEmpty()){
                //ici on fait l'appel au module Employe via la couche application
                List<EmployeDAO> employes = service.getEmployes(e.getIdEmployes());
                //on map les employés dans l'objet de retour associé et on l'ajoute à son entreprise
                entrepriseAAjouter.setEmployes(em.mapEmployeDAOToEmployeDTO(employes));
            }
            //on ajoute l'entreprise mappée dans le résultat de la requête
            entreprisesRetournees.add(entrepriseAAjouter);
        }
        return entreprisesRetournees;
    }

    @POST
    @Consumes("application/json")
    public void creationEntreprise(CreationEntrepriseDTO entrepriseDTO){
        Entreprise entrepriseToSave = new EntrepriseMapper().mapEntrepriseDTOToEntreprise(entrepriseDTO);
        service.creationEntreprise(entrepriseToSave);
    }
}