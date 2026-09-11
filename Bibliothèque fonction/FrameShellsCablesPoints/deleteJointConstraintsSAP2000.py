# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 00:00:00 2026

@author: damien.balmer
"""

def deleteJointConstraintsSAP2000(SapModel, name_filter):
    """
    This function deletes all the joint constraints whose name contains a given substring.
    Input:
        - SapModel: SAP Model object
        - name_filter: Substring that must be contained in the constraint name for it to be deleted e.g. 'Ent_Entretoise axe_'

    Output:
        - deleted_constraints: List of the names of the constraints that were deleted
    """

    # Get all defined joint constraint names
    constraint_names = list(SapModel.ConstraintDef.GetNameList()[1])

    # Delete constraints whose name contains the filter
    deleted_constraints = []
    for name in constraint_names:
        if name_filter in name:
            ret = SapModel.ConstraintDef.Delete(name)
            if ret == 0:
                deleted_constraints.append(name)

    return deleted_constraints
