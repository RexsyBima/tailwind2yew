
# tailwind2yew

A python program that transform [tailwindui components](https://tailwindui.com/) into Rust's yew view macro, uses [PydanticAI Agent Framework](https://ai.pydantic.dev/), and [Free Gemini Flash Model](https://deepmind.google/technologies/gemini/flash/).




## Installation

Install tailwind2yew with python environment already activated is highly recommended, [check them here](https://docs.python.org/3/library/venv.html). Then run below command

```bash
  pip install -r requirements.txt
```

## Environment Variables

After that, create new .env file and fill the Gemini Flash API like this, you can get them in this [link](https://aistudio.google.com/prompts/new_chat?model=gemini-1.5-flash)

`GEMINI_API_KEY`
## Demo

TOMORROW 


## Usage
1. Create empty input.txt file and put the tailwindui html component into it
`input.txt`
```
<!-- Card -->
<a class="block border border-gray-200 rounded-lg hover:shadow-sm focus:outline-none dark:border-neutral-700" href="#">
  <div class="relative flex items-center overflow-hidden">
    <img class="w-32 sm:w-48 h-full absolute inset-0 object-cover rounded-s-lg" src="https://images.unsplash.com/photo-1661956600655-e772b2b97db4?q=80&w=560&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Blog Image">

    <div class="grow p-4 ms-32 sm:ms-48">
      <div class="min-h-24 flex flex-col justify-center">
        <h3 class="font-semibold text-sm text-gray-800 dark:text-neutral-300">
          Studio by Mailchimp
        </h3>
        <p class="mt-1 text-sm text-gray-500 dark:text-neutral-500">
          Produce professional, reliable streams easily leveraging Mailchimp's innovative broadcast studio.
        </p>
      </div>
    </div>
  </div>
</a>
<!-- End Card -->
```
2. then run main.py
3. the output file will be in output.txt
`output.txt`
```rust
use yew::prelude::*;

fn blog_post_link() -> Html {
    html! {
        <a class="block border border-gray-200 rounded-lg hover:shadow-sm focus:outline-none dark:border-neutral-700" href="#">
            <div class="relative flex items-center overflow-hidden">
                <img class="w-32 sm:w-48 h-full absolute inset-0 object-cover rounded-s-lg" src="https://images.unsplash.com/photo-1661956600655-e772b2b97db4?q=80&w=560&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Blog Image"/>
                <div class="grow p-4 ms-32 sm:ms-48">
                    <div class="min-h-24 flex flex-col justify-center">
                        <h3 class="font-semibold text-sm text-gray-800 dark:text-neutral-300">
                            {"Studio by Mailchimp"}
                        </h3>
                        <p class="mt-1 text-sm text-gray-500 dark:text-neutral-500">
                            {"Produce professional, reliable streams easily leveraging Mailchimp's innovative broadcast studio."}
                        </p>
                    </div>
                </div>
            </div>
        </a>
    }
}
```
4. Then you can use the output into your rust yew project.

## FAQ

#### Is this free?

Yes, using gemini google flash, its free, but is limited. check them out https://aistudio.google.com/plan_information
## Other Question

If you have any other question, please post it in discussion tab
