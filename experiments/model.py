# Pydantic
from typing import Optional, List
from pydantic import BaseModel, Field
from enum import Enum

class SkillType(str, Enum):
    """ SKill type"""
    TECHNICAL = 'technical'
    SOFT_SKILL = 'soft-skill'

class Skill(BaseModel):
    """Skill required for the job"""

    skill: str = Field(description="Required or preferred skill in candidate. This can be technical or soft skill ")
    skill_type: SkillType = Field(description="type of skill in candidate.")
    experience: int = Field(default=None, description="Experience associated the skill.",)
    is_required: bool = Field(default = True, description="Is this skill required or preferred")    

class Skills(BaseModel):
    """Extracted skills from resume"""
    skills: List[Skill]

class Experience(BaseModel):
    """Required years of experience and the specific areas of experience sought"""
    experience: str = Field(description=(
        "Detail the required years of experience and the specific areas of experience sought (e.g., "
        "5+ years of experience in software development," 
        "3+ years of experience in project management within the healthcare industry"
        "Experience with testing frameworks"
        "). Note the context of the experience.  "
    ))
    is_required: bool = Field(default = True, description="Is this required or preferred")    

class Qualification(BaseModel):
    """Extract qualifications/ education from resume"""
    degree: str = Field(description=(
        "Specify the necessary educational background (e.g., Bachelor's degree in Computer Science, "
        "Master's degree in Business Administration) "
        "or any required certifications or licenses (e.g., PMP, CPA, AWS Certified Solutions Architect). Be exact"
    ))
    is_required: bool = Field(default = True, description="Is this qualification required or preferred")    

class PersonalityTrait(BaseModel):
    """Specific personality trait present in job description"""
    trait: str = Field(description="Specific personality traits present in job description")

class ResumeFields(BaseModel):
    skills: List[Skill] = Field(description="List of all the skills")
    experiences: List[Experience]= Field(description="List of all the experiences")
    qualifications: List[Qualification] = Field(description="List of all the qualifications")
    personality_traits: List[PersonalityTrait] = Field(description="List of all the personality traits")
    
# structured_llm = llm.with_structured_output(Skills)
# structured_llm.invoke(linkedin_target_resume)