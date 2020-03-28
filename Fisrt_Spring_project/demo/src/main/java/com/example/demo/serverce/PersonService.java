package com.example.demo.serverce;

import com.example.demo.dao.PersonDao;
import com.example.demo.model.Person;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service    // 作为服务
public class PersonService {

    private final PersonDao personDao;

    @Autowired  //自动连线
    public PersonService(@Qualifier("postgres") PersonDao personDao) {
        // 有ID，自动添加
        this.personDao = personDao;
    }

    public int addPerson(Person person){
        // 无ID，自动生成
        return personDao.insertPerson(person);
    }

    public List<Person> getAllPeople(){
        return personDao.selectAllPeople();
    }

    public Optional<Person> getPersonById(UUID id){
        return personDao.selectPersonById(id);
    }

    public int deletePerson(UUID id){
        return personDao.deletePersonById(id);
    }

    public int updatePerson(UUID id, Person newPerson){
        return personDao.updatePersonById(id, newPerson);
    }
}
