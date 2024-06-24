# Copyright 2021 Rosalind Franklin Institute
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.


# Utility imports
import unittest
import pathlib as pl
import subprocess
from glob import glob


# Test imports
import Ot2Rec
from Ot2Rec import user_args as uaMod
from Ot2Rec import params as pMod
from Ot2Rec import metadata as mMod


class metadataTest(unittest.TestCase):
    """
    Tests the Metadata functions work in O2R
    """

    def setUp(self):
        self.proj_name = "test"

    
    def test_get_param(self):
        """
        Method to test O2R.metadata:Metadata:get_param function.
        """
        # Create master param file first
        parser = uaMod.get_args_new_proj()
        args = parser.parse_args([self.proj_name])
        pMod.new_master_yaml(args)

        # Create metadata object
        meta = mMod.Metadata(project_name=self.proj_name,
                             job_type='master')

        # Test if the project name has been passed to the internal Param object successfully
        self.assertEqual(meta.prmObj.project_name, self.proj_name)

        # Test if the parameters in master yaml file has been passed successfully
        self.assertEqual(meta.params['file_prefix'], self.proj_name)

        
        
