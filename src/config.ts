export type Education = {
  place: string;
  city: string;
  date: string;
  what: string;
  thesis?: string;
};

export type Work = {
  date: string;
  title: string;
  where: string;
  city: string;
  description: string[];
  stack: string[];
};

export type Asset = "kaeiog";

export type Publication = {
  title: string;
  date: string;
  journal: string;
  abstract?: string;
  asset?: Asset;
};

export type Talk = {
  where: string;
  date: string;
  title: string;
  presentation?: string;
  url?: string;
};

export type Technology = {
  languages?: string[];
  backend?: string[];
  data_storage?: string[];
  cloud_infra?: string[];
  workflow_data_processing?: string[];
  other?: string[];
};

export type Config = {
  name: string;
  email: string;
  phone: string;
  github: string;
  linkedin: string;

  about_me: string[];
  core_skills?: string[];
  technology?: Technology;

  work: Work[];
  education?: Education[];
  publications?: Publication[];
  talks?: Talk[];
  interests?: string[];
};
