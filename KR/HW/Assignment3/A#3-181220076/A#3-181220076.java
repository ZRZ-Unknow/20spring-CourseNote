package owlapi.fhkb.fspopulation;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;

import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.io.OWLXMLOntologyFormat;
import org.semanticweb.owlapi.model.*;
import org.semanticweb.owlapi.util.DefaultPrefixManager;

import java.util.*;


/**
 * Nanjing University<br>
 * School of Artificial Intelligence<br>
 * KRistal Group<br>
 * 
 * Acknowledgement: with great thanks to Nico for his kindness & useful suggestions in making this project. 
 *
 * This class MUST HAVE A ZERO ARGUMENT CONSTRUCTOR!
 */

public class CW3 {

    private static String NAMESPACE = "http://www.cs.manchester.ac.uk/pgt/COMP60421/FamilyHistory#";

    protected CW3() {
        // Do not specify a different constructor to this empty constructor!
    }
    
    class person_beans{
    	//the beans belong to one person
    	private List <JobDataBean> beans=new ArrayList<JobDataBean>();
    	
    	public person_beans() {}
    	
    	public List<JobDataBean> getBeans() {
    		return beans;
    	}
    	
    	public void addBean(JobDataBean bean) {
    		this.beans.add(bean);
    	}
    }
    
    protected List<person_beans> collectBeansOfPerson(Collection<JobDataBean> beans){
    	//collect the beans of each person into person_beans
    	List<String> identity_list = new ArrayList<String>();
    	List<person_beans> person = new ArrayList<person_beans>();
    	for (JobDataBean bean : beans) {
    		String iden=bean.getGivenName()+" "+bean.getSurname()+" "+bean.getBirthYear();
    		if (identity_list.contains(iden)) {
    			person_beans pb=person.get(person.size()-1);
    			pb.addBean(bean);
    		}
    		else {
    			person_beans pb=new person_beans();
    			pb.addBean(bean);
    			identity_list.add(iden);
    			person.add(pb);
    			
    		}
    	}
    	return person;
    }
    
    @SuppressWarnings("unused")
	protected void populateOntology(OWLOntologyManager manager, OWLOntology ontology, Collection<JobDataBean> beans) {
    	// implement
    	OWLDataFactory df = manager.getOWLDataFactory();
    	OWLClass person_class = df.getOWLClass(IRI.create(NAMESPACE+"Person"));
    	OWLClass role_class = df.getOWLClass(IRI.create(NAMESPACE+"Role"));
    	OWLClass roleplayed_class = df.getOWLClass(IRI.create(NAMESPACE+"RolePlayed"));
    	OWLClass source_class = df.getOWLClass(IRI.create(NAMESPACE+"Source"));
    	OWLClass birth_record_class = df.getOWLClass(IRI.create(NAMESPACE+"BirthRecord"));
    	OWLClass census_class = df.getOWLClass(IRI.create(NAMESPACE+"Census"));
    	OWLClass death_record_class = df.getOWLClass(IRI.create(NAMESPACE+"DeathRecord"));
    	OWLClass marriage_record_class = df.getOWLClass(IRI.create(NAMESPACE+"MarriageRecord"));
    	OWLClass service_record_class = df.getOWLClass(IRI.create(NAMESPACE+"ServiceRecord"));
    	OWLObjectProperty plays_role = df.getOWLObjectProperty(IRI.create(NAMESPACE+"playsRole"));
    	OWLObjectProperty has_source = df.getOWLObjectProperty(IRI.create(NAMESPACE+"hasSource"));
    	OWLObjectProperty has_role = df.getOWLObjectProperty(IRI.create(NAMESPACE+"hasRole"));
    	OWLDataProperty has_surname = df.getOWLDataProperty(IRI.create(NAMESPACE+"hasSurname"));
    	OWLDataProperty has_given_name = df.getOWLDataProperty(IRI.create(NAMESPACE+"hasGivenName"));
    	OWLDataProperty has_married_surname = df.getOWLDataProperty(IRI.create(NAMESPACE+"hasMarriedSurname"));
    	OWLDataProperty has_birthyear = df.getOWLDataProperty(IRI.create(NAMESPACE+"hasBirthYear"));
    	OWLDataProperty has_year = df.getOWLDataProperty(IRI.create(NAMESPACE+"hasYear"));
    	OWLClass[] source_class_list= {birth_record_class,census_class,death_record_class,marriage_record_class,service_record_class};
    	String[] source_list = {"birthSource","censusSource","deathSource","marriageSource","serviceSource"};
    	String[] source_describe_list = {"birth","census","death","marriage","service"};
    	int person_num = 0;
    	int role_num = 0;
    	
    	List<person_beans> person = collectBeansOfPerson(beans);
    	
    	for (person_beans pb : person) {
    		String person_name = "person"+String.valueOf(++person_num);
    		OWLIndividual person_indiv = df.getOWLNamedIndividual(IRI.create(NAMESPACE+person_name));
    		OWLClassAssertionAxiom person_axiom = df.getOWLClassAssertionAxiom(person_class,person_indiv);
    		manager.addAxiom(ontology,person_axiom);
    		
    		boolean initialize = false;
    		for (JobDataBean bean : pb.getBeans()) {
    		    if (initialize==false) {
    		    	OWLDataPropertyAssertionAxiom has_given_name_axiom = 
    		    			df.getOWLDataPropertyAssertionAxiom(has_given_name, person_indiv, bean.getGivenName());
    		    	manager.addAxiom(ontology, has_given_name_axiom);
    		    	OWLDataPropertyAssertionAxiom has_surname_axiom = 
    		    			df.getOWLDataPropertyAssertionAxiom(has_surname, person_indiv, bean.getSurname());
    		    	manager.addAxiom(ontology, has_surname_axiom);
    		    	if (bean.getMarriedSurname()!=null) {
    		    		OWLDataPropertyAssertionAxiom has_married_surname_axiom = 
        		    			df.getOWLDataPropertyAssertionAxiom(has_married_surname, person_indiv, bean.getMarriedSurname());
        		    	manager.addAxiom(ontology, has_married_surname_axiom);
    		    	}
    		    	if (bean.getBirthYear()!=null) {
    		    		OWLDataPropertyAssertionAxiom has_birthyear_axiom = 
        		    			df.getOWLDataPropertyAssertionAxiom(has_birthyear, person_indiv, bean.getBirthYear());
        		    	manager.addAxiom(ontology, has_birthyear_axiom);
    		    	}
    		    	initialize=true;
    		    }
    		    if (bean.getYear()!=null) {
    		    	String roleplayed_name = "role"+String.valueOf(++role_num);
    		    	OWLIndividual roleplayed_indiv = df.getOWLNamedIndividual(IRI.create(NAMESPACE+roleplayed_name));
    		    	OWLClassAssertionAxiom roleplayed_axiom = df.getOWLClassAssertionAxiom(roleplayed_class,roleplayed_indiv);
    		    	manager.addAxiom(ontology,roleplayed_axiom);
    		    	OWLDataPropertyAssertionAxiom has_year_axiom = 
    		    			df.getOWLDataPropertyAssertionAxiom(has_year, roleplayed_indiv, bean.getYear());
    		    	manager.addAxiom(ontology, has_year_axiom);    		
    		    	OWLObjectPropertyAssertionAxiom plays_role_axiom = 
    		    			df.getOWLObjectPropertyAssertionAxiom(plays_role, person_indiv, roleplayed_indiv);
    		    	manager.addAxiom(ontology, plays_role_axiom);
    		    	
    		    	for(int i=0;i<5;i++) {
    		    		if(bean.getSource().contains(source_describe_list[i])) {
    		    			OWLIndividual source_indiv = df.getOWLNamedIndividual(IRI.create(NAMESPACE+source_list[i]));
    		    	    	OWLClassAssertionAxiom source_axiom = df.getOWLClassAssertionAxiom(source_class_list[i], source_indiv);
    		    	    	manager.addAxiom(ontology, source_axiom);
    		    	    	OWLObjectPropertyAssertionAxiom has_source_axiom = 
    	    		   				df.getOWLObjectPropertyAssertionAxiom(has_source, roleplayed_indiv, source_indiv);
    	    		   		manager.addAxiom(ontology, has_source_axiom);
    		    		}
    		    	}	
    		    	String role_string = bean.getOccupation().replaceAll(" ", "_");
    		    	OWLIndividual role_indiv = df.getOWLNamedIndividual(IRI.create(NAMESPACE+role_string+"-indiv"));
		    	    OWLClassAssertionAxiom subrole_axiom = null;
		    	    if(role_string.contentEquals("none_given")) {
		    	    	subrole_axiom = df.getOWLClassAssertionAxiom(role_class,role_indiv);
		    	    }
		    	    else {
		    	    	OWLClass subrole_class = df.getOWLClass(IRI.create(NAMESPACE+role_string));
		    	    	subrole_axiom = df.getOWLClassAssertionAxiom(subrole_class,role_indiv);
		    	    }
		    	    manager.addAxiom(ontology, subrole_axiom);
		    	    OWLObjectPropertyAssertionAxiom has_role_axiom =
		    	    		df.getOWLObjectPropertyAssertionAxiom(has_role, roleplayed_indiv, role_indiv);
		    	    manager.addAxiom(ontology, has_role_axiom);
    		    }
    		}
    	}
    	
    }
    
	protected OWLOntology loadOntology(OWLOntologyManager manager, InputStream inputStream){
    	//implement
    	OWLOntology O = null;
		try {
			O = manager.loadOntologyFromOntologyDocument(inputStream);
		} catch (OWLOntologyCreationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	return O;
    }
    
    protected void saveOntology(OWLOntologyManager manager, OWLOntology ontology, IRI locationIRI){
    	// implement
        try {
			manager.saveOntology(ontology, locationIRI);
		} catch (OWLOntologyStorageException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    }

}

