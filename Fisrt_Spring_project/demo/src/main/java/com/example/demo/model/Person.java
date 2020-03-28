package com.example.demo.model;

import com.fasterxml.jackson.annotation.JsonProperty;

import javax.validation.constraints.NotBlank;
import java.util.UUID;

public class Person {
    private final UUID id;
    @NotBlank
    private final String name;

    // 定义数据类型，人有身份ID和名字, JSON 格式
    public Person(@JsonProperty("id") UUID id,
                  @JsonProperty("name") String name){
        this.id =id;
        this.name = name;
    }

    public UUID getId(){
        return id;
    }

    public String getName(){
        return name;
    }


}
