from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import os

import numpy as np


class FormsExamplePiece(BasePiece):
    """
    This Piece serves as a simple example, from where you can start writing your own Piece.
    Remember to also change all other required files accordingly:
    - piece.py (this file)
    - models.py
    - metadata.json
    - requirements.txt or Dockerfile if needed
    """
    
    def piece_function(self, input_model: InputModel):

        # Input arguments are retrieved from the Input model object
        enum_var = input_model.enum_value
        float_var = input_model.float_value
        int_vat = input_model.int_value
        string_var = input_model.string_value
        boolean_var = input_model.boolean_value

        # Finally, results should return as an Output model
        return OutputModel(
            enum_output=enum_var,
            float_output=float_var,
            int_output=int_vat,
            string_output=string_var,
            boolean_output=boolean_var
        )