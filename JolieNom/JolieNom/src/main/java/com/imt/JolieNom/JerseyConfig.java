package com.imt.JolieNom;

import com.imt.JolieNom.presentation.EntreprisePresentation;
import jakarta.ws.rs.ApplicationPath;
import org.glassfish.jersey.server.ResourceConfig;
import org.springframework.context.annotation.Configuration;
import org.springframework.stereotype.Component;


@Component
//donne un chemin de base aux liens qui vont être exposés
@ApplicationPath("api")
//indique à Spring que le composant qui va être créé qu'il s'agit d'une configuration
@Configuration
public class JerseyConfig extends ResourceConfig {
    public JerseyConfig(){
        //enregistre la classe où les webservices vont être exposés
        register(EntreprisePresentation.class);
    }
}