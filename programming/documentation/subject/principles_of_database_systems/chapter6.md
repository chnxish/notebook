# 数据库安全与保护

## 数据库完整性

  + 完整性约束的作用对象

    - 列级约束：对于列的类型、取值范围、精度等的约束。

    - 元组约束：指元组各个字段之间的相互约束，比如开始日期小于结束日期。

    - 表级约束：指若干元组、关系之间的联系的的约束。

  + 实体完整性

    - 主键用primary key添加约束。

      - primary key(field_name),

    - 候选键用unique key进行约束。

      - unique key key_name(field_name),

  + 参照完整性：指两个表之间的关系

    - 外键用foreign key进行约束。

      - foreign key(field_name) references other_table_name(other_field_name) on delete restrict on update restrict,

  + 用户自定义完整性

    - 非空

      - id int not null auto_increment,

    - 检查约束

      - check(age>=18 and age<=60),

  + 更新完整性约束

    - alter table table_name add constraint constraint_name primary key(field_name);

    - alter table table_name add constraint constraint_name unique key(field_name);

    - alter table table_name add constraint constraint_name foreign key(field_name) references other_table_name(other_field_name);

  + 删除完整性约束

    - alter table table_name drop foreign key field_name;

    - alter table table_name drop primary key;

    - alter table table_name drop field_name;

## 触发器

  + 触发器：保护表数据的数据库对象，当指定的表发生Insert，Update，Delete时触发，进行相关的动作。

  + 创建触发器：create trigger trigger_name trigger_time trigger_event on table_name for each row trigger_statement;

    - trigger_time: before, after

    - trigger_event: insert, update, delete

```sql
create trigger test_add after insert on test for each row set @x=NEW.id;
create trigger test_del after delete on test for each row set @y=OLD.id;
```

  + 删除触发器：drop trigger trigger_name;

## 安全性与访问控制

## 事务与并发控制

## 备份与恢复
