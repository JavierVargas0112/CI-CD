package com.imt.JolieNom.presentation;

import java.util.ArrayList;
import java.util.List;

import com.imt.JolieNom.application.Entreprise;
import com.imt.JolieNom.application.EmployeDAO;

public class EntrepriseMapper {

    public EntrepriseDTO mapEntrepriseToEntrepriseDTO(Entreprise entreprise){
        EntrepriseDTO dto = new EntrepriseDTO();
        dto.setId(entreprise.getId());
        dto.setNom(entreprise.getNom());
        return dto;
    }

    public Entreprise mapEntrepriseDTOToEntreprise(CreationEntrepriseDTO entrepriseDTO){
        return new Entreprise(entrepriseDTO.getId(), entrepriseDTO.getNom(), entrepriseDTO.getIdEmployes());
    }

    public List<EmployeDTO> mapEmployeDAOToEmployeDTO(List<EmployeDAO> employes){
        List<EmployeDTO> employesDTO = new ArrayList<>();
        for(EmployeDAO e : employes){
            employesDTO.add(new EmployeDTO(e.getId(), e.getNom()));
        }
        return employesDTO;
    }
}