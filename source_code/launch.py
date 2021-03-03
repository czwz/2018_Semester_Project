from utils import get_lowdimfinder_results, get_single_lowdimfinder_results, get_filter_duplicate_structures_results

out_put_file = open('vdW_new', 'w')
groups = Group.get("testset_1_vdw_layered_3D_COD")

print('test group: structures_3d_maxphases_test', file=out_put_file)
print('', file=out_put_file)

lowdimfinder_parameter = {'bond_margins': [0],
                          'radii_offsets': [0.5],
                          'lowdim_dict': # dictionary with lowdimfinder parameters,
                                {'rotation': True, # rotation = True puts the layer plane on x-y
                                 'vacuum_space': 40.,
                                 'radii_source': 'alvarez',
                                 'orthogonal_axis_2D': False,
                                 'full_periodicity': False,
                                },
                          'target_dimensionality': 2,
                          'output': {
                                        'parent_structure_with_layer_lattice': False,
                                        'rotated_parent_structure': False,
                                        'group_data': True,
                                    },
                          }

for member in groups.nodes:

	structure = load_node(member.pk)
	ParameterData = DataFactory('parameter')
	lowdimfinder_params = ParameterData(dict=lowdimfinder_parameter)
	lowdimfinder_result_dict =  get_lowdimfinder_results(structure=structure,parameters=lowdimfinder_params,store=True)

	if len(lowdimfinder_result_dict) > 1:
		print("{:<25} & layered".format(member.get_formula()), file=out_put_file)
	else:
		print("{:<25} & not layered".format(member.get_formula()), file=out_put_file)
