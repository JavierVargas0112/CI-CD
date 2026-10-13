package com.imt.JolieNom.infrastructure;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Component;

import com.imt.JolieNom.application.Entreprise;
//permet à Spring de créer l'objet et de le configurer correctement
@Component
//ici on indique à JPARepository qu'on manipule des objets Entreprise
//et ces derniers possèdent un identifiant en format entier
public interface EntrepriseRepository extends JpaRepository<Entreprise, Integer>{
}