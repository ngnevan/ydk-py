""" Cisco_IOS_XR_pbr_vservice_ea_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pbr\-vservice\-ea package operational data.

This module contains definitions
for the following management objects\:
  service\-function\-chaining\: NSH Service Function Chaining
    operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class VsNshStats(Enum):
    """
    VsNshStats (Enum Class)

    Vs nsh stats

    .. data:: vs_nsh_stats_spi_si = 0

    	vs nsh stats spi si

    .. data:: vs_nsh_stats_ter_min_ate = 1

    	vs nsh stats ter min ate

    .. data:: vs_nsh_stats_sf = 2

    	vs nsh stats sf

    .. data:: vs_nsh_stats_sff = 3

    	vs nsh stats sff

    .. data:: vs_nsh_stats_sff_local = 4

    	vs nsh stats sff local

    .. data:: vs_nsh_stats_sfp = 5

    	vs nsh stats sfp

    .. data:: vs_nsh_stats_sfp_detail = 6

    	vs nsh stats sfp detail

    .. data:: vs_nsh_stats_max = 7

    	vs nsh stats max

    """

    vs_nsh_stats_spi_si = Enum.YLeaf(0, "vs-nsh-stats-spi-si")

    vs_nsh_stats_ter_min_ate = Enum.YLeaf(1, "vs-nsh-stats-ter-min-ate")

    vs_nsh_stats_sf = Enum.YLeaf(2, "vs-nsh-stats-sf")

    vs_nsh_stats_sff = Enum.YLeaf(3, "vs-nsh-stats-sff")

    vs_nsh_stats_sff_local = Enum.YLeaf(4, "vs-nsh-stats-sff-local")

    vs_nsh_stats_sfp = Enum.YLeaf(5, "vs-nsh-stats-sfp")

    vs_nsh_stats_sfp_detail = Enum.YLeaf(6, "vs-nsh-stats-sfp-detail")

    vs_nsh_stats_max = Enum.YLeaf(7, "vs-nsh-stats-max")



class ServiceFunctionChaining(Entity):
    """
    NSH Service Function Chaining operational data
    
    .. attribute:: nodes
    
    	Node\-specific NSH Service Function Chaining operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes>`
    
    

    """

    _prefix = 'pbr-vservice-ea-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(ServiceFunctionChaining, self).__init__()
        self._top_entity = None

        self.yang_name = "service-function-chaining"
        self.yang_parent_name = "Cisco-IOS-XR-pbr-vservice-ea-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", ServiceFunctionChaining.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = ServiceFunctionChaining.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-pbr-vservice-ea-oper:service-function-chaining"


    class Nodes(Entity):
        """
        Node\-specific NSH Service Function Chaining
        operational data
        
        .. attribute:: node
        
        	NSH operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node>`
        
        

        """

        _prefix = 'pbr-vservice-ea-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ServiceFunctionChaining.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "service-function-chaining"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", ServiceFunctionChaining.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-ea-oper:service-function-chaining/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ServiceFunctionChaining.Nodes, [], name, value)


        class Node(Entity):
            """
            NSH operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node to collect statistics from
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: process
            
            	Client Process
            	**type**\:  :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process>`
            
            

            """

            _prefix = 'pbr-vservice-ea-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ServiceFunctionChaining.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("process", ("process", ServiceFunctionChaining.Nodes.Node.Process))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.process = ServiceFunctionChaining.Nodes.Node.Process()
                self.process.parent = self
                self._children_name_map["process"] = "process"
                self._children_yang_names.add("process")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-pbr-vservice-ea-oper:service-function-chaining/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ServiceFunctionChaining.Nodes.Node, ['node_name'], name, value)


            class Process(Entity):
                """
                Client Process
                
                .. attribute:: service_function_path
                
                	Service Function Path operational data
                	**type**\:  :py:class:`ServiceFunctionPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath>`
                
                .. attribute:: service_function
                
                	Service Function operational data
                	**type**\:  :py:class:`ServiceFunction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction>`
                
                .. attribute:: service_function_forwarder
                
                	Service Function Forwarder operational data
                	**type**\:  :py:class:`ServiceFunctionForwarder <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder>`
                
                

                """

                _prefix = 'pbr-vservice-ea-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ServiceFunctionChaining.Nodes.Node.Process, self).__init__()

                    self.yang_name = "process"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("service-function-path", ("service_function_path", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath)), ("service-function", ("service_function", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction)), ("service-function-forwarder", ("service_function_forwarder", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.service_function_path = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath()
                    self.service_function_path.parent = self
                    self._children_name_map["service_function_path"] = "service-function-path"
                    self._children_yang_names.add("service-function-path")

                    self.service_function = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction()
                    self.service_function.parent = self
                    self._children_name_map["service_function"] = "service-function"
                    self._children_yang_names.add("service-function")

                    self.service_function_forwarder = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder()
                    self.service_function_forwarder.parent = self
                    self._children_name_map["service_function_forwarder"] = "service-function-forwarder"
                    self._children_yang_names.add("service-function-forwarder")
                    self._segment_path = lambda: "process"


                class ServiceFunctionPath(Entity):
                    """
                    Service Function Path operational data
                    
                    .. attribute:: path_ids
                    
                    	Service Function Path Id 
                    	**type**\:  :py:class:`PathIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds>`
                    
                    

                    """

                    _prefix = 'pbr-vservice-ea-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath, self).__init__()

                        self.yang_name = "service-function-path"
                        self.yang_parent_name = "process"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("path-ids", ("path_ids", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.path_ids = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds()
                        self.path_ids.parent = self
                        self._children_name_map["path_ids"] = "path-ids"
                        self._children_yang_names.add("path-ids")
                        self._segment_path = lambda: "service-function-path"


                    class PathIds(Entity):
                        """
                        Service Function Path Id 
                        
                        .. attribute:: path_id
                        
                        	Specific Service\-Function\-Path identifier 
                        	**type**\: list of  		 :py:class:`PathId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId>`
                        
                        

                        """

                        _prefix = 'pbr-vservice-ea-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds, self).__init__()

                            self.yang_name = "path-ids"
                            self.yang_parent_name = "service-function-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("path-id", ("path_id", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId))])
                            self._leafs = OrderedDict()

                            self.path_id = YList(self)
                            self._segment_path = lambda: "path-ids"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds, [], name, value)


                        class PathId(Entity):
                            """
                            Specific Service\-Function\-Path identifier 
                            
                            .. attribute:: id  (key)
                            
                            	Specific Service\-Function\-Path identifier
                            	**type**\: int
                            
                            	**range:** 1..16777215
                            
                            .. attribute:: service_indexes
                            
                            	Service Index Belonging to Path
                            	**type**\:  :py:class:`ServiceIndexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes>`
                            
                            .. attribute:: stats
                            
                            	SFP Statistics
                            	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats>`
                            
                            

                            """

                            _prefix = 'pbr-vservice-ea-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId, self).__init__()

                                self.yang_name = "path-id"
                                self.yang_parent_name = "path-ids"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['id']
                                self._child_container_classes = OrderedDict([("service-indexes", ("service_indexes", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes)), ("stats", ("stats", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('id', YLeaf(YType.uint32, 'id')),
                                ])
                                self.id = None

                                self.service_indexes = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes()
                                self.service_indexes.parent = self
                                self._children_name_map["service_indexes"] = "service-indexes"
                                self._children_yang_names.add("service-indexes")

                                self.stats = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats()
                                self.stats.parent = self
                                self._children_name_map["stats"] = "stats"
                                self._children_yang_names.add("stats")
                                self._segment_path = lambda: "path-id" + "[id='" + str(self.id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId, ['id'], name, value)


                            class ServiceIndexes(Entity):
                                """
                                Service Index Belonging to Path
                                
                                .. attribute:: service_index
                                
                                	Service index operational data belonging to this path
                                	**type**\: list of  		 :py:class:`ServiceIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes, self).__init__()

                                    self.yang_name = "service-indexes"
                                    self.yang_parent_name = "path-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("service-index", ("service_index", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex))])
                                    self._leafs = OrderedDict()

                                    self.service_index = YList(self)
                                    self._segment_path = lambda: "service-indexes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes, [], name, value)


                                class ServiceIndex(Entity):
                                    """
                                    Service index operational data belonging
                                    to this path
                                    
                                    .. attribute:: index  (key)
                                    
                                    	Service Index
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    .. attribute:: data
                                    
                                    	Statistics data
                                    	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data>`
                                    
                                    .. attribute:: si_arr
                                    
                                    	SI array in case of detail stats
                                    	**type**\: list of  		 :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex, self).__init__()

                                        self.yang_name = "service-index"
                                        self.yang_parent_name = "service-indexes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['index']
                                        self._child_container_classes = OrderedDict([("data", ("data", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data))])
                                        self._child_list_classes = OrderedDict([("si-arr", ("si_arr", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr))])
                                        self._leafs = OrderedDict([
                                            ('index', YLeaf(YType.uint32, 'index')),
                                        ])
                                        self.index = None

                                        self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data()
                                        self.data.parent = self
                                        self._children_name_map["data"] = "data"
                                        self._children_yang_names.add("data")

                                        self.si_arr = YList(self)
                                        self._segment_path = lambda: "service-index" + "[index='" + str(self.index) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex, ['index'], name, value)


                                    class Data(Entity):
                                        """
                                        Statistics data
                                        
                                        .. attribute:: sfp
                                        
                                        	SFP stats
                                        	**type**\:  :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp>`
                                        
                                        .. attribute:: spi_si
                                        
                                        	SPI SI stats
                                        	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi>`
                                        
                                        .. attribute:: term
                                        
                                        	Terminate stats
                                        	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term>`
                                        
                                        .. attribute:: sf
                                        
                                        	Service function stats
                                        	**type**\:  :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf>`
                                        
                                        .. attribute:: sff
                                        
                                        	Service function forwarder stats
                                        	**type**\:  :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff>`
                                        
                                        .. attribute:: sff_local
                                        
                                        	Local service function forwarder stats
                                        	**type**\:  :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal>`
                                        
                                        .. attribute:: type
                                        
                                        	type
                                        	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data, self).__init__()

                                            self.yang_name = "data"
                                            self.yang_parent_name = "service-index"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("sfp", ("sfp", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp)), ("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term)), ("sf", ("sf", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf)), ("sff", ("sff", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff)), ("sff-local", ("sff_local", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('type', YLeaf(YType.enumeration, 'type')),
                                            ])
                                            self.type = None

                                            self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp()
                                            self.sfp.parent = self
                                            self._children_name_map["sfp"] = "sfp"
                                            self._children_yang_names.add("sfp")

                                            self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi()
                                            self.spi_si.parent = self
                                            self._children_name_map["spi_si"] = "spi-si"
                                            self._children_yang_names.add("spi-si")

                                            self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term()
                                            self.term.parent = self
                                            self._children_name_map["term"] = "term"
                                            self._children_yang_names.add("term")

                                            self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf()
                                            self.sf.parent = self
                                            self._children_name_map["sf"] = "sf"
                                            self._children_yang_names.add("sf")

                                            self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff()
                                            self.sff.parent = self
                                            self._children_name_map["sff"] = "sff"
                                            self._children_yang_names.add("sff")

                                            self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal()
                                            self.sff_local.parent = self
                                            self._children_name_map["sff_local"] = "sff-local"
                                            self._children_yang_names.add("sff-local")
                                            self._segment_path = lambda: "data"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data, ['type'], name, value)


                                        class Sfp(Entity):
                                            """
                                            SFP stats
                                            
                                            .. attribute:: spi_si
                                            
                                            	Service index counters
                                            	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate counters
                                            	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp, self).__init__()

                                                self.yang_name = "sfp"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict()

                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                                self._children_yang_names.add("spi-si")

                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                                self._children_yang_names.add("term")
                                                self._segment_path = lambda: "sfp"


                                            class SpiSi(Entity):
                                                """
                                                Service index counters
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2017-05-01'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi, self).__init__()

                                                    self.yang_name = "spi-si"
                                                    self.yang_parent_name = "sfp"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                        ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                    ])
                                                    self.processed_pkts = None
                                                    self.processed_bytes = None
                                                    self._segment_path = lambda: "spi-si"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                            class Term(Entity):
                                                """
                                                Terminate counters
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2017-05-01'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term, self).__init__()

                                                    self.yang_name = "term"
                                                    self.yang_parent_name = "sfp"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                        ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                                    ])
                                                    self.terminated_pkts = None
                                                    self.terminated_bytes = None
                                                    self._segment_path = lambda: "term"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sfp.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                                        class SpiSi(Entity):
                                            """
                                            SPI SI stats
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi, self).__init__()

                                                self.yang_name = "spi-si"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                    ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                ])
                                                self.processed_pkts = None
                                                self.processed_bytes = None
                                                self._segment_path = lambda: "spi-si"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                        class Term(Entity):
                                            """
                                            Terminate stats
                                            
                                            .. attribute:: terminated_pkts
                                            
                                            	Number of terminated packets
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: terminated_bytes
                                            
                                            	Total bytes terminated
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term, self).__init__()

                                                self.yang_name = "term"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                    ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                                ])
                                                self.terminated_pkts = None
                                                self.terminated_bytes = None
                                                self._segment_path = lambda: "term"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                                        class Sf(Entity):
                                            """
                                            Service function stats
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf, self).__init__()

                                                self.yang_name = "sf"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                    ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                ])
                                                self.processed_pkts = None
                                                self.processed_bytes = None
                                                self._segment_path = lambda: "sf"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sf, ['processed_pkts', 'processed_bytes'], name, value)


                                        class Sff(Entity):
                                            """
                                            Service function forwarder stats
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff, self).__init__()

                                                self.yang_name = "sff"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                    ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                ])
                                                self.processed_pkts = None
                                                self.processed_bytes = None
                                                self._segment_path = lambda: "sff"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.Sff, ['processed_pkts', 'processed_bytes'], name, value)


                                        class SffLocal(Entity):
                                            """
                                            Local service function forwarder stats
                                            
                                            .. attribute:: malformed_err_pkts
                                            
                                            	Number of packets with invalid NSH header
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: lookup_err_pkts
                                            
                                            	Number of packets with unknown spi\-si
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: malformed_err_bytes
                                            
                                            	Total bytes with invalid NSH header
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: lookup_err_bytes
                                            
                                            	Total bytes with unknown spi\-si
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal, self).__init__()

                                                self.yang_name = "sff-local"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('malformed_err_pkts', YLeaf(YType.uint64, 'malformed-err-pkts')),
                                                    ('lookup_err_pkts', YLeaf(YType.uint64, 'lookup-err-pkts')),
                                                    ('malformed_err_bytes', YLeaf(YType.uint64, 'malformed-err-bytes')),
                                                    ('lookup_err_bytes', YLeaf(YType.uint64, 'lookup-err-bytes')),
                                                ])
                                                self.malformed_err_pkts = None
                                                self.lookup_err_pkts = None
                                                self.malformed_err_bytes = None
                                                self.lookup_err_bytes = None
                                                self._segment_path = lambda: "sff-local"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.Data.SffLocal, ['malformed_err_pkts', 'lookup_err_pkts', 'malformed_err_bytes', 'lookup_err_bytes'], name, value)


                                    class SiArr(Entity):
                                        """
                                        SI array in case of detail stats
                                        
                                        .. attribute:: data
                                        
                                        	Stats counter for this index
                                        	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data>`
                                        
                                        .. attribute:: si
                                        
                                        	Service index
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr, self).__init__()

                                            self.yang_name = "si-arr"
                                            self.yang_parent_name = "service-index"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("data", ("data", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('si', YLeaf(YType.uint8, 'si')),
                                            ])
                                            self.si = None

                                            self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data()
                                            self.data.parent = self
                                            self._children_name_map["data"] = "data"
                                            self._children_yang_names.add("data")
                                            self._segment_path = lambda: "si-arr"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr, ['si'], name, value)


                                        class Data(Entity):
                                            """
                                            Stats counter for this index
                                            
                                            .. attribute:: spi_si
                                            
                                            	SF/SFF stats
                                            	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate stats
                                            	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term>`
                                            
                                            .. attribute:: type
                                            
                                            	type
                                            	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data, self).__init__()

                                                self.yang_name = "data"
                                                self.yang_parent_name = "si-arr"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('type', YLeaf(YType.enumeration, 'type')),
                                                ])
                                                self.type = None

                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                                self._children_yang_names.add("spi-si")

                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                                self._children_yang_names.add("term")
                                                self._segment_path = lambda: "data"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data, ['type'], name, value)


                                            class SpiSi(Entity):
                                                """
                                                SF/SFF stats
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2017-05-01'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi, self).__init__()

                                                    self.yang_name = "spi-si"
                                                    self.yang_parent_name = "data"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                        ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                    ])
                                                    self.processed_pkts = None
                                                    self.processed_bytes = None
                                                    self._segment_path = lambda: "spi-si"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                            class Term(Entity):
                                                """
                                                Terminate stats
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2017-05-01'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term, self).__init__()

                                                    self.yang_name = "term"
                                                    self.yang_parent_name = "data"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                        ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                                    ])
                                                    self.terminated_pkts = None
                                                    self.terminated_bytes = None
                                                    self._segment_path = lambda: "term"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.ServiceIndexes.ServiceIndex.SiArr.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                            class Stats(Entity):
                                """
                                SFP Statistics
                                
                                .. attribute:: detail
                                
                                	Detail statistics per service index 
                                	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail>`
                                
                                .. attribute:: summarized
                                
                                	Combined statistics of all service index in service functionpath
                                	**type**\:  :py:class:`Summarized <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats, self).__init__()

                                    self.yang_name = "stats"
                                    self.yang_parent_name = "path-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("detail", ("detail", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail)), ("summarized", ("summarized", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.detail = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail()
                                    self.detail.parent = self
                                    self._children_name_map["detail"] = "detail"
                                    self._children_yang_names.add("detail")

                                    self.summarized = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized()
                                    self.summarized.parent = self
                                    self._children_name_map["summarized"] = "summarized"
                                    self._children_yang_names.add("summarized")
                                    self._segment_path = lambda: "stats"


                                class Detail(Entity):
                                    """
                                    Detail statistics per service index 
                                    
                                    .. attribute:: data
                                    
                                    	Statistics data
                                    	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data>`
                                    
                                    .. attribute:: si_arr
                                    
                                    	SI array in case of detail stats
                                    	**type**\: list of  		 :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail, self).__init__()

                                        self.yang_name = "detail"
                                        self.yang_parent_name = "stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("data", ("data", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data))])
                                        self._child_list_classes = OrderedDict([("si-arr", ("si_arr", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr))])
                                        self._leafs = OrderedDict()

                                        self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data()
                                        self.data.parent = self
                                        self._children_name_map["data"] = "data"
                                        self._children_yang_names.add("data")

                                        self.si_arr = YList(self)
                                        self._segment_path = lambda: "detail"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail, [], name, value)


                                    class Data(Entity):
                                        """
                                        Statistics data
                                        
                                        .. attribute:: sfp
                                        
                                        	SFP stats
                                        	**type**\:  :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp>`
                                        
                                        .. attribute:: spi_si
                                        
                                        	SPI SI stats
                                        	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi>`
                                        
                                        .. attribute:: term
                                        
                                        	Terminate stats
                                        	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term>`
                                        
                                        .. attribute:: sf
                                        
                                        	Service function stats
                                        	**type**\:  :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf>`
                                        
                                        .. attribute:: sff
                                        
                                        	Service function forwarder stats
                                        	**type**\:  :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff>`
                                        
                                        .. attribute:: sff_local
                                        
                                        	Local service function forwarder stats
                                        	**type**\:  :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal>`
                                        
                                        .. attribute:: type
                                        
                                        	type
                                        	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data, self).__init__()

                                            self.yang_name = "data"
                                            self.yang_parent_name = "detail"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("sfp", ("sfp", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp)), ("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term)), ("sf", ("sf", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf)), ("sff", ("sff", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff)), ("sff-local", ("sff_local", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('type', YLeaf(YType.enumeration, 'type')),
                                            ])
                                            self.type = None

                                            self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp()
                                            self.sfp.parent = self
                                            self._children_name_map["sfp"] = "sfp"
                                            self._children_yang_names.add("sfp")

                                            self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi()
                                            self.spi_si.parent = self
                                            self._children_name_map["spi_si"] = "spi-si"
                                            self._children_yang_names.add("spi-si")

                                            self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term()
                                            self.term.parent = self
                                            self._children_name_map["term"] = "term"
                                            self._children_yang_names.add("term")

                                            self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf()
                                            self.sf.parent = self
                                            self._children_name_map["sf"] = "sf"
                                            self._children_yang_names.add("sf")

                                            self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff()
                                            self.sff.parent = self
                                            self._children_name_map["sff"] = "sff"
                                            self._children_yang_names.add("sff")

                                            self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal()
                                            self.sff_local.parent = self
                                            self._children_name_map["sff_local"] = "sff-local"
                                            self._children_yang_names.add("sff-local")
                                            self._segment_path = lambda: "data"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data, ['type'], name, value)


                                        class Sfp(Entity):
                                            """
                                            SFP stats
                                            
                                            .. attribute:: spi_si
                                            
                                            	Service index counters
                                            	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate counters
                                            	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp, self).__init__()

                                                self.yang_name = "sfp"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict()

                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                                self._children_yang_names.add("spi-si")

                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                                self._children_yang_names.add("term")
                                                self._segment_path = lambda: "sfp"


                                            class SpiSi(Entity):
                                                """
                                                Service index counters
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2017-05-01'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi, self).__init__()

                                                    self.yang_name = "spi-si"
                                                    self.yang_parent_name = "sfp"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                        ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                    ])
                                                    self.processed_pkts = None
                                                    self.processed_bytes = None
                                                    self._segment_path = lambda: "spi-si"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                            class Term(Entity):
                                                """
                                                Terminate counters
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2017-05-01'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term, self).__init__()

                                                    self.yang_name = "term"
                                                    self.yang_parent_name = "sfp"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                        ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                                    ])
                                                    self.terminated_pkts = None
                                                    self.terminated_bytes = None
                                                    self._segment_path = lambda: "term"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sfp.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                                        class SpiSi(Entity):
                                            """
                                            SPI SI stats
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi, self).__init__()

                                                self.yang_name = "spi-si"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                    ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                ])
                                                self.processed_pkts = None
                                                self.processed_bytes = None
                                                self._segment_path = lambda: "spi-si"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                        class Term(Entity):
                                            """
                                            Terminate stats
                                            
                                            .. attribute:: terminated_pkts
                                            
                                            	Number of terminated packets
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: terminated_bytes
                                            
                                            	Total bytes terminated
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term, self).__init__()

                                                self.yang_name = "term"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                    ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                                ])
                                                self.terminated_pkts = None
                                                self.terminated_bytes = None
                                                self._segment_path = lambda: "term"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                                        class Sf(Entity):
                                            """
                                            Service function stats
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf, self).__init__()

                                                self.yang_name = "sf"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                    ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                ])
                                                self.processed_pkts = None
                                                self.processed_bytes = None
                                                self._segment_path = lambda: "sf"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sf, ['processed_pkts', 'processed_bytes'], name, value)


                                        class Sff(Entity):
                                            """
                                            Service function forwarder stats
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff, self).__init__()

                                                self.yang_name = "sff"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                    ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                ])
                                                self.processed_pkts = None
                                                self.processed_bytes = None
                                                self._segment_path = lambda: "sff"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.Sff, ['processed_pkts', 'processed_bytes'], name, value)


                                        class SffLocal(Entity):
                                            """
                                            Local service function forwarder stats
                                            
                                            .. attribute:: malformed_err_pkts
                                            
                                            	Number of packets with invalid NSH header
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: lookup_err_pkts
                                            
                                            	Number of packets with unknown spi\-si
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: malformed_err_bytes
                                            
                                            	Total bytes with invalid NSH header
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: lookup_err_bytes
                                            
                                            	Total bytes with unknown spi\-si
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal, self).__init__()

                                                self.yang_name = "sff-local"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('malformed_err_pkts', YLeaf(YType.uint64, 'malformed-err-pkts')),
                                                    ('lookup_err_pkts', YLeaf(YType.uint64, 'lookup-err-pkts')),
                                                    ('malformed_err_bytes', YLeaf(YType.uint64, 'malformed-err-bytes')),
                                                    ('lookup_err_bytes', YLeaf(YType.uint64, 'lookup-err-bytes')),
                                                ])
                                                self.malformed_err_pkts = None
                                                self.lookup_err_pkts = None
                                                self.malformed_err_bytes = None
                                                self.lookup_err_bytes = None
                                                self._segment_path = lambda: "sff-local"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.Data.SffLocal, ['malformed_err_pkts', 'lookup_err_pkts', 'malformed_err_bytes', 'lookup_err_bytes'], name, value)


                                    class SiArr(Entity):
                                        """
                                        SI array in case of detail stats
                                        
                                        .. attribute:: data
                                        
                                        	Stats counter for this index
                                        	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data>`
                                        
                                        .. attribute:: si
                                        
                                        	Service index
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr, self).__init__()

                                            self.yang_name = "si-arr"
                                            self.yang_parent_name = "detail"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("data", ("data", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('si', YLeaf(YType.uint8, 'si')),
                                            ])
                                            self.si = None

                                            self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data()
                                            self.data.parent = self
                                            self._children_name_map["data"] = "data"
                                            self._children_yang_names.add("data")
                                            self._segment_path = lambda: "si-arr"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr, ['si'], name, value)


                                        class Data(Entity):
                                            """
                                            Stats counter for this index
                                            
                                            .. attribute:: spi_si
                                            
                                            	SF/SFF stats
                                            	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate stats
                                            	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term>`
                                            
                                            .. attribute:: type
                                            
                                            	type
                                            	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data, self).__init__()

                                                self.yang_name = "data"
                                                self.yang_parent_name = "si-arr"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('type', YLeaf(YType.enumeration, 'type')),
                                                ])
                                                self.type = None

                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                                self._children_yang_names.add("spi-si")

                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                                self._children_yang_names.add("term")
                                                self._segment_path = lambda: "data"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data, ['type'], name, value)


                                            class SpiSi(Entity):
                                                """
                                                SF/SFF stats
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2017-05-01'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi, self).__init__()

                                                    self.yang_name = "spi-si"
                                                    self.yang_parent_name = "data"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                        ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                    ])
                                                    self.processed_pkts = None
                                                    self.processed_bytes = None
                                                    self._segment_path = lambda: "spi-si"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                            class Term(Entity):
                                                """
                                                Terminate stats
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2017-05-01'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term, self).__init__()

                                                    self.yang_name = "term"
                                                    self.yang_parent_name = "data"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                        ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                                    ])
                                                    self.terminated_pkts = None
                                                    self.terminated_bytes = None
                                                    self._segment_path = lambda: "term"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Detail.SiArr.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                                class Summarized(Entity):
                                    """
                                    Combined statistics of all service index
                                    in service functionpath
                                    
                                    .. attribute:: data
                                    
                                    	Statistics data
                                    	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data>`
                                    
                                    .. attribute:: si_arr
                                    
                                    	SI array in case of detail stats
                                    	**type**\: list of  		 :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized, self).__init__()

                                        self.yang_name = "summarized"
                                        self.yang_parent_name = "stats"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("data", ("data", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data))])
                                        self._child_list_classes = OrderedDict([("si-arr", ("si_arr", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr))])
                                        self._leafs = OrderedDict()

                                        self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data()
                                        self.data.parent = self
                                        self._children_name_map["data"] = "data"
                                        self._children_yang_names.add("data")

                                        self.si_arr = YList(self)
                                        self._segment_path = lambda: "summarized"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized, [], name, value)


                                    class Data(Entity):
                                        """
                                        Statistics data
                                        
                                        .. attribute:: sfp
                                        
                                        	SFP stats
                                        	**type**\:  :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp>`
                                        
                                        .. attribute:: spi_si
                                        
                                        	SPI SI stats
                                        	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi>`
                                        
                                        .. attribute:: term
                                        
                                        	Terminate stats
                                        	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term>`
                                        
                                        .. attribute:: sf
                                        
                                        	Service function stats
                                        	**type**\:  :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf>`
                                        
                                        .. attribute:: sff
                                        
                                        	Service function forwarder stats
                                        	**type**\:  :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff>`
                                        
                                        .. attribute:: sff_local
                                        
                                        	Local service function forwarder stats
                                        	**type**\:  :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal>`
                                        
                                        .. attribute:: type
                                        
                                        	type
                                        	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data, self).__init__()

                                            self.yang_name = "data"
                                            self.yang_parent_name = "summarized"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("sfp", ("sfp", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp)), ("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term)), ("sf", ("sf", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf)), ("sff", ("sff", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff)), ("sff-local", ("sff_local", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('type', YLeaf(YType.enumeration, 'type')),
                                            ])
                                            self.type = None

                                            self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp()
                                            self.sfp.parent = self
                                            self._children_name_map["sfp"] = "sfp"
                                            self._children_yang_names.add("sfp")

                                            self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi()
                                            self.spi_si.parent = self
                                            self._children_name_map["spi_si"] = "spi-si"
                                            self._children_yang_names.add("spi-si")

                                            self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term()
                                            self.term.parent = self
                                            self._children_name_map["term"] = "term"
                                            self._children_yang_names.add("term")

                                            self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf()
                                            self.sf.parent = self
                                            self._children_name_map["sf"] = "sf"
                                            self._children_yang_names.add("sf")

                                            self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff()
                                            self.sff.parent = self
                                            self._children_name_map["sff"] = "sff"
                                            self._children_yang_names.add("sff")

                                            self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal()
                                            self.sff_local.parent = self
                                            self._children_name_map["sff_local"] = "sff-local"
                                            self._children_yang_names.add("sff-local")
                                            self._segment_path = lambda: "data"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data, ['type'], name, value)


                                        class Sfp(Entity):
                                            """
                                            SFP stats
                                            
                                            .. attribute:: spi_si
                                            
                                            	Service index counters
                                            	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate counters
                                            	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp, self).__init__()

                                                self.yang_name = "sfp"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict()

                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                                self._children_yang_names.add("spi-si")

                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                                self._children_yang_names.add("term")
                                                self._segment_path = lambda: "sfp"


                                            class SpiSi(Entity):
                                                """
                                                Service index counters
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2017-05-01'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi, self).__init__()

                                                    self.yang_name = "spi-si"
                                                    self.yang_parent_name = "sfp"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                        ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                    ])
                                                    self.processed_pkts = None
                                                    self.processed_bytes = None
                                                    self._segment_path = lambda: "spi-si"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                            class Term(Entity):
                                                """
                                                Terminate counters
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2017-05-01'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term, self).__init__()

                                                    self.yang_name = "term"
                                                    self.yang_parent_name = "sfp"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                        ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                                    ])
                                                    self.terminated_pkts = None
                                                    self.terminated_bytes = None
                                                    self._segment_path = lambda: "term"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sfp.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                                        class SpiSi(Entity):
                                            """
                                            SPI SI stats
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi, self).__init__()

                                                self.yang_name = "spi-si"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                    ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                ])
                                                self.processed_pkts = None
                                                self.processed_bytes = None
                                                self._segment_path = lambda: "spi-si"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                        class Term(Entity):
                                            """
                                            Terminate stats
                                            
                                            .. attribute:: terminated_pkts
                                            
                                            	Number of terminated packets
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: terminated_bytes
                                            
                                            	Total bytes terminated
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term, self).__init__()

                                                self.yang_name = "term"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                    ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                                ])
                                                self.terminated_pkts = None
                                                self.terminated_bytes = None
                                                self._segment_path = lambda: "term"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                                        class Sf(Entity):
                                            """
                                            Service function stats
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf, self).__init__()

                                                self.yang_name = "sf"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                    ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                ])
                                                self.processed_pkts = None
                                                self.processed_bytes = None
                                                self._segment_path = lambda: "sf"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sf, ['processed_pkts', 'processed_bytes'], name, value)


                                        class Sff(Entity):
                                            """
                                            Service function forwarder stats
                                            
                                            .. attribute:: processed_pkts
                                            
                                            	Number of packets processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: processed_bytes
                                            
                                            	Total bytes processed
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff, self).__init__()

                                                self.yang_name = "sff"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                    ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                ])
                                                self.processed_pkts = None
                                                self.processed_bytes = None
                                                self._segment_path = lambda: "sff"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.Sff, ['processed_pkts', 'processed_bytes'], name, value)


                                        class SffLocal(Entity):
                                            """
                                            Local service function forwarder stats
                                            
                                            .. attribute:: malformed_err_pkts
                                            
                                            	Number of packets with invalid NSH header
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: lookup_err_pkts
                                            
                                            	Number of packets with unknown spi\-si
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: malformed_err_bytes
                                            
                                            	Total bytes with invalid NSH header
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            .. attribute:: lookup_err_bytes
                                            
                                            	Total bytes with unknown spi\-si
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            	**units**\: byte
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal, self).__init__()

                                                self.yang_name = "sff-local"
                                                self.yang_parent_name = "data"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('malformed_err_pkts', YLeaf(YType.uint64, 'malformed-err-pkts')),
                                                    ('lookup_err_pkts', YLeaf(YType.uint64, 'lookup-err-pkts')),
                                                    ('malformed_err_bytes', YLeaf(YType.uint64, 'malformed-err-bytes')),
                                                    ('lookup_err_bytes', YLeaf(YType.uint64, 'lookup-err-bytes')),
                                                ])
                                                self.malformed_err_pkts = None
                                                self.lookup_err_pkts = None
                                                self.malformed_err_bytes = None
                                                self.lookup_err_bytes = None
                                                self._segment_path = lambda: "sff-local"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.Data.SffLocal, ['malformed_err_pkts', 'lookup_err_pkts', 'malformed_err_bytes', 'lookup_err_bytes'], name, value)


                                    class SiArr(Entity):
                                        """
                                        SI array in case of detail stats
                                        
                                        .. attribute:: data
                                        
                                        	Stats counter for this index
                                        	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data>`
                                        
                                        .. attribute:: si
                                        
                                        	Service index
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr, self).__init__()

                                            self.yang_name = "si-arr"
                                            self.yang_parent_name = "summarized"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("data", ("data", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('si', YLeaf(YType.uint8, 'si')),
                                            ])
                                            self.si = None

                                            self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data()
                                            self.data.parent = self
                                            self._children_name_map["data"] = "data"
                                            self._children_yang_names.add("data")
                                            self._segment_path = lambda: "si-arr"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr, ['si'], name, value)


                                        class Data(Entity):
                                            """
                                            Stats counter for this index
                                            
                                            .. attribute:: spi_si
                                            
                                            	SF/SFF stats
                                            	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi>`
                                            
                                            .. attribute:: term
                                            
                                            	Terminate stats
                                            	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term>`
                                            
                                            .. attribute:: type
                                            
                                            	type
                                            	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                            
                                            

                                            """

                                            _prefix = 'pbr-vservice-ea-oper'
                                            _revision = '2017-05-01'

                                            def __init__(self):
                                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data, self).__init__()

                                                self.yang_name = "data"
                                                self.yang_parent_name = "si-arr"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('type', YLeaf(YType.enumeration, 'type')),
                                                ])
                                                self.type = None

                                                self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi()
                                                self.spi_si.parent = self
                                                self._children_name_map["spi_si"] = "spi-si"
                                                self._children_yang_names.add("spi-si")

                                                self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term()
                                                self.term.parent = self
                                                self._children_name_map["term"] = "term"
                                                self._children_yang_names.add("term")
                                                self._segment_path = lambda: "data"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data, ['type'], name, value)


                                            class SpiSi(Entity):
                                                """
                                                SF/SFF stats
                                                
                                                .. attribute:: processed_pkts
                                                
                                                	Number of packets processed
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: processed_bytes
                                                
                                                	Total bytes processed
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2017-05-01'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi, self).__init__()

                                                    self.yang_name = "spi-si"
                                                    self.yang_parent_name = "data"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                        ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                                    ])
                                                    self.processed_pkts = None
                                                    self.processed_bytes = None
                                                    self._segment_path = lambda: "spi-si"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                            class Term(Entity):
                                                """
                                                Terminate stats
                                                
                                                .. attribute:: terminated_pkts
                                                
                                                	Number of terminated packets
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                .. attribute:: terminated_bytes
                                                
                                                	Total bytes terminated
                                                	**type**\: int
                                                
                                                	**range:** 0..18446744073709551615
                                                
                                                	**units**\: byte
                                                
                                                

                                                """

                                                _prefix = 'pbr-vservice-ea-oper'
                                                _revision = '2017-05-01'

                                                def __init__(self):
                                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term, self).__init__()

                                                    self.yang_name = "term"
                                                    self.yang_parent_name = "data"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                        ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                                    ])
                                                    self.terminated_pkts = None
                                                    self.terminated_bytes = None
                                                    self._segment_path = lambda: "term"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionPath.PathIds.PathId.Stats.Summarized.SiArr.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                class ServiceFunction(Entity):
                    """
                    Service Function operational data
                    
                    .. attribute:: sf_names
                    
                    	List of Service Function Names
                    	**type**\:  :py:class:`SfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames>`
                    
                    

                    """

                    _prefix = 'pbr-vservice-ea-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction, self).__init__()

                        self.yang_name = "service-function"
                        self.yang_parent_name = "process"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("sf-names", ("sf_names", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.sf_names = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames()
                        self.sf_names.parent = self
                        self._children_name_map["sf_names"] = "sf-names"
                        self._children_yang_names.add("sf-names")
                        self._segment_path = lambda: "service-function"


                    class SfNames(Entity):
                        """
                        List of Service Function Names
                        
                        .. attribute:: sf_name
                        
                        	Name of Service Function
                        	**type**\: list of  		 :py:class:`SfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName>`
                        
                        

                        """

                        _prefix = 'pbr-vservice-ea-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames, self).__init__()

                            self.yang_name = "sf-names"
                            self.yang_parent_name = "service-function"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("sf-name", ("sf_name", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName))])
                            self._leafs = OrderedDict()

                            self.sf_name = YList(self)
                            self._segment_path = lambda: "sf-names"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames, [], name, value)


                        class SfName(Entity):
                            """
                            Name of Service Function
                            
                            .. attribute:: name  (key)
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            .. attribute:: data
                            
                            	Statistics data
                            	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data>`
                            
                            .. attribute:: si_arr
                            
                            	SI array in case of detail stats
                            	**type**\: list of  		 :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr>`
                            
                            

                            """

                            _prefix = 'pbr-vservice-ea-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName, self).__init__()

                                self.yang_name = "sf-name"
                                self.yang_parent_name = "sf-names"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['name']
                                self._child_container_classes = OrderedDict([("data", ("data", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data))])
                                self._child_list_classes = OrderedDict([("si-arr", ("si_arr", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr))])
                                self._leafs = OrderedDict([
                                    ('name', YLeaf(YType.str, 'name')),
                                ])
                                self.name = None

                                self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data()
                                self.data.parent = self
                                self._children_name_map["data"] = "data"
                                self._children_yang_names.add("data")

                                self.si_arr = YList(self)
                                self._segment_path = lambda: "sf-name" + "[name='" + str(self.name) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName, ['name'], name, value)


                            class Data(Entity):
                                """
                                Statistics data
                                
                                .. attribute:: sfp
                                
                                	SFP stats
                                	**type**\:  :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp>`
                                
                                .. attribute:: spi_si
                                
                                	SPI SI stats
                                	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi>`
                                
                                .. attribute:: term
                                
                                	Terminate stats
                                	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term>`
                                
                                .. attribute:: sf
                                
                                	Service function stats
                                	**type**\:  :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf>`
                                
                                .. attribute:: sff
                                
                                	Service function forwarder stats
                                	**type**\:  :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff>`
                                
                                .. attribute:: sff_local
                                
                                	Local service function forwarder stats
                                	**type**\:  :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data, self).__init__()

                                    self.yang_name = "data"
                                    self.yang_parent_name = "sf-name"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("sfp", ("sfp", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp)), ("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term)), ("sf", ("sf", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf)), ("sff", ("sff", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff)), ("sff-local", ("sff_local", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('type', YLeaf(YType.enumeration, 'type')),
                                    ])
                                    self.type = None

                                    self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp()
                                    self.sfp.parent = self
                                    self._children_name_map["sfp"] = "sfp"
                                    self._children_yang_names.add("sfp")

                                    self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi()
                                    self.spi_si.parent = self
                                    self._children_name_map["spi_si"] = "spi-si"
                                    self._children_yang_names.add("spi-si")

                                    self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term()
                                    self.term.parent = self
                                    self._children_name_map["term"] = "term"
                                    self._children_yang_names.add("term")

                                    self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf()
                                    self.sf.parent = self
                                    self._children_name_map["sf"] = "sf"
                                    self._children_yang_names.add("sf")

                                    self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff()
                                    self.sff.parent = self
                                    self._children_name_map["sff"] = "sff"
                                    self._children_yang_names.add("sff")

                                    self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal()
                                    self.sff_local.parent = self
                                    self._children_name_map["sff_local"] = "sff-local"
                                    self._children_yang_names.add("sff-local")
                                    self._segment_path = lambda: "data"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data, ['type'], name, value)


                                class Sfp(Entity):
                                    """
                                    SFP stats
                                    
                                    .. attribute:: spi_si
                                    
                                    	Service index counters
                                    	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate counters
                                    	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp, self).__init__()

                                        self.yang_name = "sfp"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict()

                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi()
                                        self.spi_si.parent = self
                                        self._children_name_map["spi_si"] = "spi-si"
                                        self._children_yang_names.add("spi-si")

                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term()
                                        self.term.parent = self
                                        self._children_name_map["term"] = "term"
                                        self._children_yang_names.add("term")
                                        self._segment_path = lambda: "sfp"


                                    class SpiSi(Entity):
                                        """
                                        Service index counters
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi, self).__init__()

                                            self.yang_name = "spi-si"
                                            self.yang_parent_name = "sfp"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                            ])
                                            self.processed_pkts = None
                                            self.processed_bytes = None
                                            self._segment_path = lambda: "spi-si"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                    class Term(Entity):
                                        """
                                        Terminate counters
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term, self).__init__()

                                            self.yang_name = "term"
                                            self.yang_parent_name = "sfp"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                            ])
                                            self.terminated_pkts = None
                                            self.terminated_bytes = None
                                            self._segment_path = lambda: "term"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sfp.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                                class SpiSi(Entity):
                                    """
                                    SPI SI stats
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi, self).__init__()

                                        self.yang_name = "spi-si"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                            ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "spi-si"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                class Term(Entity):
                                    """
                                    Terminate stats
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term, self).__init__()

                                        self.yang_name = "term"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                            ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                        ])
                                        self.terminated_pkts = None
                                        self.terminated_bytes = None
                                        self._segment_path = lambda: "term"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                                class Sf(Entity):
                                    """
                                    Service function stats
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf, self).__init__()

                                        self.yang_name = "sf"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                            ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "sf"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sf, ['processed_pkts', 'processed_bytes'], name, value)


                                class Sff(Entity):
                                    """
                                    Service function forwarder stats
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff, self).__init__()

                                        self.yang_name = "sff"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                            ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "sff"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.Sff, ['processed_pkts', 'processed_bytes'], name, value)


                                class SffLocal(Entity):
                                    """
                                    Local service function forwarder stats
                                    
                                    .. attribute:: malformed_err_pkts
                                    
                                    	Number of packets with invalid NSH header
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: lookup_err_pkts
                                    
                                    	Number of packets with unknown spi\-si
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: malformed_err_bytes
                                    
                                    	Total bytes with invalid NSH header
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: lookup_err_bytes
                                    
                                    	Total bytes with unknown spi\-si
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal, self).__init__()

                                        self.yang_name = "sff-local"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('malformed_err_pkts', YLeaf(YType.uint64, 'malformed-err-pkts')),
                                            ('lookup_err_pkts', YLeaf(YType.uint64, 'lookup-err-pkts')),
                                            ('malformed_err_bytes', YLeaf(YType.uint64, 'malformed-err-bytes')),
                                            ('lookup_err_bytes', YLeaf(YType.uint64, 'lookup-err-bytes')),
                                        ])
                                        self.malformed_err_pkts = None
                                        self.lookup_err_pkts = None
                                        self.malformed_err_bytes = None
                                        self.lookup_err_bytes = None
                                        self._segment_path = lambda: "sff-local"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.Data.SffLocal, ['malformed_err_pkts', 'lookup_err_pkts', 'malformed_err_bytes', 'lookup_err_bytes'], name, value)


                            class SiArr(Entity):
                                """
                                SI array in case of detail stats
                                
                                .. attribute:: data
                                
                                	Stats counter for this index
                                	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data>`
                                
                                .. attribute:: si
                                
                                	Service index
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr, self).__init__()

                                    self.yang_name = "si-arr"
                                    self.yang_parent_name = "sf-name"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("data", ("data", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('si', YLeaf(YType.uint8, 'si')),
                                    ])
                                    self.si = None

                                    self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data()
                                    self.data.parent = self
                                    self._children_name_map["data"] = "data"
                                    self._children_yang_names.add("data")
                                    self._segment_path = lambda: "si-arr"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr, ['si'], name, value)


                                class Data(Entity):
                                    """
                                    Stats counter for this index
                                    
                                    .. attribute:: spi_si
                                    
                                    	SF/SFF stats
                                    	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate stats
                                    	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term>`
                                    
                                    .. attribute:: type
                                    
                                    	type
                                    	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data, self).__init__()

                                        self.yang_name = "data"
                                        self.yang_parent_name = "si-arr"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('type', YLeaf(YType.enumeration, 'type')),
                                        ])
                                        self.type = None

                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi()
                                        self.spi_si.parent = self
                                        self._children_name_map["spi_si"] = "spi-si"
                                        self._children_yang_names.add("spi-si")

                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term()
                                        self.term.parent = self
                                        self._children_name_map["term"] = "term"
                                        self._children_yang_names.add("term")
                                        self._segment_path = lambda: "data"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data, ['type'], name, value)


                                    class SpiSi(Entity):
                                        """
                                        SF/SFF stats
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi, self).__init__()

                                            self.yang_name = "spi-si"
                                            self.yang_parent_name = "data"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                            ])
                                            self.processed_pkts = None
                                            self.processed_bytes = None
                                            self._segment_path = lambda: "spi-si"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                    class Term(Entity):
                                        """
                                        Terminate stats
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term, self).__init__()

                                            self.yang_name = "term"
                                            self.yang_parent_name = "data"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                            ])
                                            self.terminated_pkts = None
                                            self.terminated_bytes = None
                                            self._segment_path = lambda: "term"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunction.SfNames.SfName.SiArr.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                class ServiceFunctionForwarder(Entity):
                    """
                    Service Function Forwarder operational data
                    
                    .. attribute:: local
                    
                    	Local Service Function Forwarder operational data
                    	**type**\:  :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local>`
                    
                    .. attribute:: sff_names
                    
                    	List of Service Function Forwarder Names
                    	**type**\:  :py:class:`SffNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames>`
                    
                    

                    """

                    _prefix = 'pbr-vservice-ea-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder, self).__init__()

                        self.yang_name = "service-function-forwarder"
                        self.yang_parent_name = "process"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("local", ("local", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local)), ("sff-names", ("sff_names", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local()
                        self.local.parent = self
                        self._children_name_map["local"] = "local"
                        self._children_yang_names.add("local")

                        self.sff_names = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames()
                        self.sff_names.parent = self
                        self._children_name_map["sff_names"] = "sff-names"
                        self._children_yang_names.add("sff-names")
                        self._segment_path = lambda: "service-function-forwarder"


                    class Local(Entity):
                        """
                        Local Service Function Forwarder operational
                        data
                        
                        .. attribute:: error
                        
                        	Error Statistics for local service function forwarder
                        	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error>`
                        
                        

                        """

                        _prefix = 'pbr-vservice-ea-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local, self).__init__()

                            self.yang_name = "local"
                            self.yang_parent_name = "service-function-forwarder"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("error", ("error", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.error = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error()
                            self.error.parent = self
                            self._children_name_map["error"] = "error"
                            self._children_yang_names.add("error")
                            self._segment_path = lambda: "local"


                        class Error(Entity):
                            """
                            Error Statistics for local service function
                            forwarder
                            
                            .. attribute:: data
                            
                            	Statistics data
                            	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data>`
                            
                            .. attribute:: si_arr
                            
                            	SI array in case of detail stats
                            	**type**\: list of  		 :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr>`
                            
                            

                            """

                            _prefix = 'pbr-vservice-ea-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error, self).__init__()

                                self.yang_name = "error"
                                self.yang_parent_name = "local"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("data", ("data", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data))])
                                self._child_list_classes = OrderedDict([("si-arr", ("si_arr", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr))])
                                self._leafs = OrderedDict()

                                self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data()
                                self.data.parent = self
                                self._children_name_map["data"] = "data"
                                self._children_yang_names.add("data")

                                self.si_arr = YList(self)
                                self._segment_path = lambda: "error"

                            def __setattr__(self, name, value):
                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error, [], name, value)


                            class Data(Entity):
                                """
                                Statistics data
                                
                                .. attribute:: sfp
                                
                                	SFP stats
                                	**type**\:  :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp>`
                                
                                .. attribute:: spi_si
                                
                                	SPI SI stats
                                	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi>`
                                
                                .. attribute:: term
                                
                                	Terminate stats
                                	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term>`
                                
                                .. attribute:: sf
                                
                                	Service function stats
                                	**type**\:  :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf>`
                                
                                .. attribute:: sff
                                
                                	Service function forwarder stats
                                	**type**\:  :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff>`
                                
                                .. attribute:: sff_local
                                
                                	Local service function forwarder stats
                                	**type**\:  :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data, self).__init__()

                                    self.yang_name = "data"
                                    self.yang_parent_name = "error"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("sfp", ("sfp", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp)), ("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term)), ("sf", ("sf", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf)), ("sff", ("sff", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff)), ("sff-local", ("sff_local", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('type', YLeaf(YType.enumeration, 'type')),
                                    ])
                                    self.type = None

                                    self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp()
                                    self.sfp.parent = self
                                    self._children_name_map["sfp"] = "sfp"
                                    self._children_yang_names.add("sfp")

                                    self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi()
                                    self.spi_si.parent = self
                                    self._children_name_map["spi_si"] = "spi-si"
                                    self._children_yang_names.add("spi-si")

                                    self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term()
                                    self.term.parent = self
                                    self._children_name_map["term"] = "term"
                                    self._children_yang_names.add("term")

                                    self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf()
                                    self.sf.parent = self
                                    self._children_name_map["sf"] = "sf"
                                    self._children_yang_names.add("sf")

                                    self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff()
                                    self.sff.parent = self
                                    self._children_name_map["sff"] = "sff"
                                    self._children_yang_names.add("sff")

                                    self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal()
                                    self.sff_local.parent = self
                                    self._children_name_map["sff_local"] = "sff-local"
                                    self._children_yang_names.add("sff-local")
                                    self._segment_path = lambda: "data"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data, ['type'], name, value)


                                class Sfp(Entity):
                                    """
                                    SFP stats
                                    
                                    .. attribute:: spi_si
                                    
                                    	Service index counters
                                    	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate counters
                                    	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp, self).__init__()

                                        self.yang_name = "sfp"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict()

                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi()
                                        self.spi_si.parent = self
                                        self._children_name_map["spi_si"] = "spi-si"
                                        self._children_yang_names.add("spi-si")

                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term()
                                        self.term.parent = self
                                        self._children_name_map["term"] = "term"
                                        self._children_yang_names.add("term")
                                        self._segment_path = lambda: "sfp"


                                    class SpiSi(Entity):
                                        """
                                        Service index counters
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi, self).__init__()

                                            self.yang_name = "spi-si"
                                            self.yang_parent_name = "sfp"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                            ])
                                            self.processed_pkts = None
                                            self.processed_bytes = None
                                            self._segment_path = lambda: "spi-si"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                    class Term(Entity):
                                        """
                                        Terminate counters
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term, self).__init__()

                                            self.yang_name = "term"
                                            self.yang_parent_name = "sfp"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                            ])
                                            self.terminated_pkts = None
                                            self.terminated_bytes = None
                                            self._segment_path = lambda: "term"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sfp.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                                class SpiSi(Entity):
                                    """
                                    SPI SI stats
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi, self).__init__()

                                        self.yang_name = "spi-si"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                            ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "spi-si"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                class Term(Entity):
                                    """
                                    Terminate stats
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term, self).__init__()

                                        self.yang_name = "term"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                            ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                        ])
                                        self.terminated_pkts = None
                                        self.terminated_bytes = None
                                        self._segment_path = lambda: "term"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                                class Sf(Entity):
                                    """
                                    Service function stats
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf, self).__init__()

                                        self.yang_name = "sf"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                            ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "sf"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sf, ['processed_pkts', 'processed_bytes'], name, value)


                                class Sff(Entity):
                                    """
                                    Service function forwarder stats
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff, self).__init__()

                                        self.yang_name = "sff"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                            ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "sff"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.Sff, ['processed_pkts', 'processed_bytes'], name, value)


                                class SffLocal(Entity):
                                    """
                                    Local service function forwarder stats
                                    
                                    .. attribute:: malformed_err_pkts
                                    
                                    	Number of packets with invalid NSH header
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: lookup_err_pkts
                                    
                                    	Number of packets with unknown spi\-si
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: malformed_err_bytes
                                    
                                    	Total bytes with invalid NSH header
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: lookup_err_bytes
                                    
                                    	Total bytes with unknown spi\-si
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal, self).__init__()

                                        self.yang_name = "sff-local"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('malformed_err_pkts', YLeaf(YType.uint64, 'malformed-err-pkts')),
                                            ('lookup_err_pkts', YLeaf(YType.uint64, 'lookup-err-pkts')),
                                            ('malformed_err_bytes', YLeaf(YType.uint64, 'malformed-err-bytes')),
                                            ('lookup_err_bytes', YLeaf(YType.uint64, 'lookup-err-bytes')),
                                        ])
                                        self.malformed_err_pkts = None
                                        self.lookup_err_pkts = None
                                        self.malformed_err_bytes = None
                                        self.lookup_err_bytes = None
                                        self._segment_path = lambda: "sff-local"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.Data.SffLocal, ['malformed_err_pkts', 'lookup_err_pkts', 'malformed_err_bytes', 'lookup_err_bytes'], name, value)


                            class SiArr(Entity):
                                """
                                SI array in case of detail stats
                                
                                .. attribute:: data
                                
                                	Stats counter for this index
                                	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data>`
                                
                                .. attribute:: si
                                
                                	Service index
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr, self).__init__()

                                    self.yang_name = "si-arr"
                                    self.yang_parent_name = "error"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("data", ("data", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('si', YLeaf(YType.uint8, 'si')),
                                    ])
                                    self.si = None

                                    self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data()
                                    self.data.parent = self
                                    self._children_name_map["data"] = "data"
                                    self._children_yang_names.add("data")
                                    self._segment_path = lambda: "si-arr"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr, ['si'], name, value)


                                class Data(Entity):
                                    """
                                    Stats counter for this index
                                    
                                    .. attribute:: spi_si
                                    
                                    	SF/SFF stats
                                    	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate stats
                                    	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term>`
                                    
                                    .. attribute:: type
                                    
                                    	type
                                    	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data, self).__init__()

                                        self.yang_name = "data"
                                        self.yang_parent_name = "si-arr"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('type', YLeaf(YType.enumeration, 'type')),
                                        ])
                                        self.type = None

                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi()
                                        self.spi_si.parent = self
                                        self._children_name_map["spi_si"] = "spi-si"
                                        self._children_yang_names.add("spi-si")

                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term()
                                        self.term.parent = self
                                        self._children_name_map["term"] = "term"
                                        self._children_yang_names.add("term")
                                        self._segment_path = lambda: "data"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data, ['type'], name, value)


                                    class SpiSi(Entity):
                                        """
                                        SF/SFF stats
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi, self).__init__()

                                            self.yang_name = "spi-si"
                                            self.yang_parent_name = "data"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                            ])
                                            self.processed_pkts = None
                                            self.processed_bytes = None
                                            self._segment_path = lambda: "spi-si"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                    class Term(Entity):
                                        """
                                        Terminate stats
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term, self).__init__()

                                            self.yang_name = "term"
                                            self.yang_parent_name = "data"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                            ])
                                            self.terminated_pkts = None
                                            self.terminated_bytes = None
                                            self._segment_path = lambda: "term"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.Local.Error.SiArr.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                    class SffNames(Entity):
                        """
                        List of Service Function Forwarder Names
                        
                        .. attribute:: sff_name
                        
                        	Name of Service Function Forwarder
                        	**type**\: list of  		 :py:class:`SffName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName>`
                        
                        

                        """

                        _prefix = 'pbr-vservice-ea-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames, self).__init__()

                            self.yang_name = "sff-names"
                            self.yang_parent_name = "service-function-forwarder"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("sff-name", ("sff_name", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName))])
                            self._leafs = OrderedDict()

                            self.sff_name = YList(self)
                            self._segment_path = lambda: "sff-names"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames, [], name, value)


                        class SffName(Entity):
                            """
                            Name of Service Function Forwarder
                            
                            .. attribute:: name  (key)
                            
                            	Name
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            .. attribute:: data
                            
                            	Statistics data
                            	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data>`
                            
                            .. attribute:: si_arr
                            
                            	SI array in case of detail stats
                            	**type**\: list of  		 :py:class:`SiArr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr>`
                            
                            

                            """

                            _prefix = 'pbr-vservice-ea-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName, self).__init__()

                                self.yang_name = "sff-name"
                                self.yang_parent_name = "sff-names"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['name']
                                self._child_container_classes = OrderedDict([("data", ("data", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data))])
                                self._child_list_classes = OrderedDict([("si-arr", ("si_arr", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr))])
                                self._leafs = OrderedDict([
                                    ('name', YLeaf(YType.str, 'name')),
                                ])
                                self.name = None

                                self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data()
                                self.data.parent = self
                                self._children_name_map["data"] = "data"
                                self._children_yang_names.add("data")

                                self.si_arr = YList(self)
                                self._segment_path = lambda: "sff-name" + "[name='" + str(self.name) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName, ['name'], name, value)


                            class Data(Entity):
                                """
                                Statistics data
                                
                                .. attribute:: sfp
                                
                                	SFP stats
                                	**type**\:  :py:class:`Sfp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp>`
                                
                                .. attribute:: spi_si
                                
                                	SPI SI stats
                                	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi>`
                                
                                .. attribute:: term
                                
                                	Terminate stats
                                	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term>`
                                
                                .. attribute:: sf
                                
                                	Service function stats
                                	**type**\:  :py:class:`Sf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf>`
                                
                                .. attribute:: sff
                                
                                	Service function forwarder stats
                                	**type**\:  :py:class:`Sff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff>`
                                
                                .. attribute:: sff_local
                                
                                	Local service function forwarder stats
                                	**type**\:  :py:class:`SffLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data, self).__init__()

                                    self.yang_name = "data"
                                    self.yang_parent_name = "sff-name"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("sfp", ("sfp", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp)), ("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term)), ("sf", ("sf", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf)), ("sff", ("sff", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff)), ("sff-local", ("sff_local", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('type', YLeaf(YType.enumeration, 'type')),
                                    ])
                                    self.type = None

                                    self.sfp = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp()
                                    self.sfp.parent = self
                                    self._children_name_map["sfp"] = "sfp"
                                    self._children_yang_names.add("sfp")

                                    self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi()
                                    self.spi_si.parent = self
                                    self._children_name_map["spi_si"] = "spi-si"
                                    self._children_yang_names.add("spi-si")

                                    self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term()
                                    self.term.parent = self
                                    self._children_name_map["term"] = "term"
                                    self._children_yang_names.add("term")

                                    self.sf = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf()
                                    self.sf.parent = self
                                    self._children_name_map["sf"] = "sf"
                                    self._children_yang_names.add("sf")

                                    self.sff = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff()
                                    self.sff.parent = self
                                    self._children_name_map["sff"] = "sff"
                                    self._children_yang_names.add("sff")

                                    self.sff_local = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal()
                                    self.sff_local.parent = self
                                    self._children_name_map["sff_local"] = "sff-local"
                                    self._children_yang_names.add("sff-local")
                                    self._segment_path = lambda: "data"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data, ['type'], name, value)


                                class Sfp(Entity):
                                    """
                                    SFP stats
                                    
                                    .. attribute:: spi_si
                                    
                                    	Service index counters
                                    	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate counters
                                    	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp, self).__init__()

                                        self.yang_name = "sfp"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict()

                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi()
                                        self.spi_si.parent = self
                                        self._children_name_map["spi_si"] = "spi-si"
                                        self._children_yang_names.add("spi-si")

                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term()
                                        self.term.parent = self
                                        self._children_name_map["term"] = "term"
                                        self._children_yang_names.add("term")
                                        self._segment_path = lambda: "sfp"


                                    class SpiSi(Entity):
                                        """
                                        Service index counters
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi, self).__init__()

                                            self.yang_name = "spi-si"
                                            self.yang_parent_name = "sfp"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                            ])
                                            self.processed_pkts = None
                                            self.processed_bytes = None
                                            self._segment_path = lambda: "spi-si"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                    class Term(Entity):
                                        """
                                        Terminate counters
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term, self).__init__()

                                            self.yang_name = "term"
                                            self.yang_parent_name = "sfp"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                            ])
                                            self.terminated_pkts = None
                                            self.terminated_bytes = None
                                            self._segment_path = lambda: "term"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sfp.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                                class SpiSi(Entity):
                                    """
                                    SPI SI stats
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi, self).__init__()

                                        self.yang_name = "spi-si"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                            ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "spi-si"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                class Term(Entity):
                                    """
                                    Terminate stats
                                    
                                    .. attribute:: terminated_pkts
                                    
                                    	Number of terminated packets
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: terminated_bytes
                                    
                                    	Total bytes terminated
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term, self).__init__()

                                        self.yang_name = "term"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                            ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                        ])
                                        self.terminated_pkts = None
                                        self.terminated_bytes = None
                                        self._segment_path = lambda: "term"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)


                                class Sf(Entity):
                                    """
                                    Service function stats
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf, self).__init__()

                                        self.yang_name = "sf"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                            ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "sf"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sf, ['processed_pkts', 'processed_bytes'], name, value)


                                class Sff(Entity):
                                    """
                                    Service function forwarder stats
                                    
                                    .. attribute:: processed_pkts
                                    
                                    	Number of packets processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: processed_bytes
                                    
                                    	Total bytes processed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff, self).__init__()

                                        self.yang_name = "sff"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                            ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                        ])
                                        self.processed_pkts = None
                                        self.processed_bytes = None
                                        self._segment_path = lambda: "sff"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.Sff, ['processed_pkts', 'processed_bytes'], name, value)


                                class SffLocal(Entity):
                                    """
                                    Local service function forwarder stats
                                    
                                    .. attribute:: malformed_err_pkts
                                    
                                    	Number of packets with invalid NSH header
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: lookup_err_pkts
                                    
                                    	Number of packets with unknown spi\-si
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: malformed_err_bytes
                                    
                                    	Total bytes with invalid NSH header
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: lookup_err_bytes
                                    
                                    	Total bytes with unknown spi\-si
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal, self).__init__()

                                        self.yang_name = "sff-local"
                                        self.yang_parent_name = "data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('malformed_err_pkts', YLeaf(YType.uint64, 'malformed-err-pkts')),
                                            ('lookup_err_pkts', YLeaf(YType.uint64, 'lookup-err-pkts')),
                                            ('malformed_err_bytes', YLeaf(YType.uint64, 'malformed-err-bytes')),
                                            ('lookup_err_bytes', YLeaf(YType.uint64, 'lookup-err-bytes')),
                                        ])
                                        self.malformed_err_pkts = None
                                        self.lookup_err_pkts = None
                                        self.malformed_err_bytes = None
                                        self.lookup_err_bytes = None
                                        self._segment_path = lambda: "sff-local"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.Data.SffLocal, ['malformed_err_pkts', 'lookup_err_pkts', 'malformed_err_bytes', 'lookup_err_bytes'], name, value)


                            class SiArr(Entity):
                                """
                                SI array in case of detail stats
                                
                                .. attribute:: data
                                
                                	Stats counter for this index
                                	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data>`
                                
                                .. attribute:: si
                                
                                	Service index
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'pbr-vservice-ea-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr, self).__init__()

                                    self.yang_name = "si-arr"
                                    self.yang_parent_name = "sff-name"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("data", ("data", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('si', YLeaf(YType.uint8, 'si')),
                                    ])
                                    self.si = None

                                    self.data = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data()
                                    self.data.parent = self
                                    self._children_name_map["data"] = "data"
                                    self._children_yang_names.add("data")
                                    self._segment_path = lambda: "si-arr"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr, ['si'], name, value)


                                class Data(Entity):
                                    """
                                    Stats counter for this index
                                    
                                    .. attribute:: spi_si
                                    
                                    	SF/SFF stats
                                    	**type**\:  :py:class:`SpiSi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi>`
                                    
                                    .. attribute:: term
                                    
                                    	Terminate stats
                                    	**type**\:  :py:class:`Term <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term>`
                                    
                                    .. attribute:: type
                                    
                                    	type
                                    	**type**\:  :py:class:`VsNshStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_vservice_ea_oper.VsNshStats>`
                                    
                                    

                                    """

                                    _prefix = 'pbr-vservice-ea-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data, self).__init__()

                                        self.yang_name = "data"
                                        self.yang_parent_name = "si-arr"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("spi-si", ("spi_si", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi)), ("term", ("term", ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('type', YLeaf(YType.enumeration, 'type')),
                                        ])
                                        self.type = None

                                        self.spi_si = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi()
                                        self.spi_si.parent = self
                                        self._children_name_map["spi_si"] = "spi-si"
                                        self._children_yang_names.add("spi-si")

                                        self.term = ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term()
                                        self.term.parent = self
                                        self._children_name_map["term"] = "term"
                                        self._children_yang_names.add("term")
                                        self._segment_path = lambda: "data"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data, ['type'], name, value)


                                    class SpiSi(Entity):
                                        """
                                        SF/SFF stats
                                        
                                        .. attribute:: processed_pkts
                                        
                                        	Number of packets processed
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: processed_bytes
                                        
                                        	Total bytes processed
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi, self).__init__()

                                            self.yang_name = "spi-si"
                                            self.yang_parent_name = "data"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('processed_pkts', YLeaf(YType.uint64, 'processed-pkts')),
                                                ('processed_bytes', YLeaf(YType.uint64, 'processed-bytes')),
                                            ])
                                            self.processed_pkts = None
                                            self.processed_bytes = None
                                            self._segment_path = lambda: "spi-si"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.SpiSi, ['processed_pkts', 'processed_bytes'], name, value)


                                    class Term(Entity):
                                        """
                                        Terminate stats
                                        
                                        .. attribute:: terminated_pkts
                                        
                                        	Number of terminated packets
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: terminated_bytes
                                        
                                        	Total bytes terminated
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        

                                        """

                                        _prefix = 'pbr-vservice-ea-oper'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term, self).__init__()

                                            self.yang_name = "term"
                                            self.yang_parent_name = "data"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('terminated_pkts', YLeaf(YType.uint64, 'terminated-pkts')),
                                                ('terminated_bytes', YLeaf(YType.uint64, 'terminated-bytes')),
                                            ])
                                            self.terminated_pkts = None
                                            self.terminated_bytes = None
                                            self._segment_path = lambda: "term"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(ServiceFunctionChaining.Nodes.Node.Process.ServiceFunctionForwarder.SffNames.SffName.SiArr.Data.Term, ['terminated_pkts', 'terminated_bytes'], name, value)

    def clone_ptr(self):
        self._top_entity = ServiceFunctionChaining()
        return self._top_entity

