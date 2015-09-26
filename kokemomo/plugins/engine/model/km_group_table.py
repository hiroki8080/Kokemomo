#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_storage.impl.km_rdb_adapter import adapter

__author__ = 'hiroki'

"""
It is the accessor to group table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    name:String
    parent:Integer
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

[Basic Usage]
You can use the each method from the acquisition of the session in getSession ().

-example-----------------------------------------------------------
from lib.kmgrouptable import get_session,add,find,find_all,delete

def search_parameter():
    session = get_session()
    result = find_all(session)
    session.close()
    return result

-------------------------------------------------------------------
"""


class KMGroup(adapter.Model):
    __tablename__ = 'km_group'
    id = adapter.Column(adapter.Integer, autoincrement=True, primary_key=True)
    name = adapter.Column(adapter.String(50))
    parent_id = adapter.Column(adapter.Integer)

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)


def find(id, session):
    pass
    """
    Find the group.
    :param id: group id.
    :param session: session
    :return: group data.
    """
    result = None
    for group in session.query(KMGroup).filter_by(id=id).all():
        result = group
    return result


def find_all(session):
    pass
    """
    Find all the groups.
    :param session: session
    :return: group data.
    """
    result = []
    fetch = session.query(KMGroup)
    for group in fetch.all():
        result.append(group)
    return result


def add(group, session):
    pass
    """
    Add the group
    :param group: group model
    :param session: session
    """
    try:
        session.add(group)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def update(group, session):
    pass
    """
    Update the group.
    :param group: group model
    :param session: session
    """
    try:
        session.merge(group)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def delete(id, session):
    pass
    """
    Delete the group.
    :param id: group id
    :param session: session
    """
    fetch_object = session.query(KMGroup).filter_by(id=id).one()
    try:
        session.delete(fetch_object)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
