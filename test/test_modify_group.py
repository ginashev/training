from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group_name1", header="group_head1", footer="group_foot1"))
    old_groups = app.group.get_group_list()
    group = Group(name="group_name2", header="group_head2", footer="group_foot2")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group_name1", header="group_head1", footer="group_foot1"))
    old_groups = app.group.get_group_list()
    group = Group(name="New header")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


