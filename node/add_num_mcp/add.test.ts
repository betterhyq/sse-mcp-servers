import { expect, test } from "vitest";
import { add } from "./add";

test("add", () => {
  expect(add({ a: 1, b: 2 })).toBe("3");
});
