import { z } from "zod";
import { FastMCP } from "fastmcp";

export const main = (port: number) => {
  const server = new FastMCP({
    name: "Add Num MCP",
    version: "1.0.0",
  });

  server.addTool({
    name: "add",
    description: "Add two numbers",
    parameters: z.object({
      a: z.number(),
      b: z.number(),
    }),
    execute: async (args) => {
      return String(args.a + args.b);
    },
  });

  server.start({
    transportType: "httpStream",
    httpStream: {
      host: "0.0.0.0",
      port: port,
    },
  });
};
