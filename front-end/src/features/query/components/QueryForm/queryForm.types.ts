import type { FC } from "react";

export type QueryFormComponent = FC<{
  onDomainChange: (domain: string) => void;
}>;
