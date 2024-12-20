from day_5_p2 import steps_of_move, move_crate, move_crates, top_crates
import unittest 
import pytest 

def test_steps_of_move():
    # Given
    instruction = 'move 1 from 2 to 1'
    expected_instruction = (1,2,1)
    # When
    actual_instruction = steps_of_move(instruction=instruction) 
    # Then
    assert expected_instruction==actual_instruction

def test_move_crate():
    # GIVEN
    crate_stacks = [                                                 
        ['Z','N'],['M','C','D'],['P']      
    ]
    move_instruction = (1, 2, 1)
    expected_crates = [
        ['Z','N','D'],['M','C'],['P']
    ]
    # WHEN
    actual_crates = move_crate(crate_stacks=crate_stacks,move_instruction=move_instruction) 
    # THEN
    assert expected_crates==actual_crates 


def test_move_crates():
    # GIVEN
    crate_stacks = [                                                 
        ['Z','N'],['M','C','D'],['P']  
    ]
    instructions = ['move 1 from 2 to 1','move 3 from 1 to 3','move 2 from 2 to 1','move 1 from 1 to 2']
    expected_crates = [['M'],['C'],['P','Z','N','D']]

    # WHEN
    actual_crates = move_crates(crate_stacks=crate_stacks, move_instructions=instructions)
    
    # THEN
    assert expected_crates==actual_crates

def test_top_crates():
    # GIVEN 
    crate_stacks = [['C'],['M'],['P','D','N','Z']]
    expected_outcome = 'CMZ'

    # WHEN
    actual_outcome = top_crates(crates=crate_stacks)

    # THEN
    assert actual_outcome == expected_outcome