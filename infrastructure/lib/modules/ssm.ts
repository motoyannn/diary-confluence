import * as cdk from "aws-cdk-lib";

import * as ssm from "aws-cdk-lib/aws-ssm";

type Props = {};

export const createSSM = (stack: cdk.Stack, props: Props) => {
  createParameters(stack, {});
  return;
};

type ParameterStoreProps = {};
const createParameters = (stack: cdk.Stack, props: ParameterStoreProps) => {
  new ssm.StringParameter(stack, "ConfluenceUrlParameterStore", {
    allowedPattern: ".*",
    description: "Confluence URL",
    parameterName: "/automation/confluence/URL",
    stringValue: process.env.CONFLUENCE_URL || "",
    tier: ssm.ParameterTier.STANDARD,
  });
  new ssm.StringParameter(stack, "ConfluenceUserParameterStore", {
    allowedPattern: ".*",
    description: "Confluence User",
    parameterName: "/automation/confluence/USER",
    stringValue: process.env.CONFLUENCE_USER || "",
    tier: ssm.ParameterTier.STANDARD,
  });
  new ssm.StringParameter(stack, "ConfluenceTokenParameterStore", {
    allowedPattern: ".*",
    description: "Confluence Token",
    parameterName: "/automation/confluence/TOKEN",
    stringValue: process.env.CONFLUENCE_TOKEN || "",
    tier: ssm.ParameterTier.STANDARD,
  });
  new ssm.StringParameter(stack, "ConfluenceSpaceParameterStore", {
    allowedPattern: ".*",
    description: "Confluence Space",
    parameterName: "/automation/confluence/SPACE",
    stringValue: process.env.CONFLUENCE_SPACE || "",
    tier: ssm.ParameterTier.STANDARD,
  });
  new ssm.StringParameter(stack, "ConfluenceParentPageParameterStore", {
    allowedPattern: ".*",
    description: "Confluence Parent Page",
    parameterName: "/automation/confluence/PARENT_PAGE",
    stringValue: process.env.CONFLUENCE_PARENT_PAGE || "",
    tier: ssm.ParameterTier.STANDARD,
  });
};
