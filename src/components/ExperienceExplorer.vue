<script setup lang="ts">
//Experience Explorer
import { ref, computed } from 'vue';
import ExperienceItem from "./ExperienceItem.vue";

interface Experience {
  id: string;
  role: string;
  company: string;
  dates: string;
  achievements: string[];
  technologies?: string[];
  type: 'Full-time' | 'Part-time' | 'Contract' | 'Freelance' | 'Internship';
  location: string;
  icon: string;
  dateModified: string;
  duration: string;
  size: string; // For display purposes (e.g., "2.3 years")
}

interface Props {
  experiences?: Experience[];
  isOpen: boolean;
}

const emit = defineEmits<{
  (e: 'update:isOpen', value: boolean): void;
}>();

function toggleOpen() {
  emit('update:isOpen', !props.isOpen);
}

const props = withDefaults(defineProps<Props>(), {
  experiences: () => [
    {
      id: '1',
      role: 'Senior Frontend Developer',
      company: 'TechCorp Solutions',
      dates: '2023-01 - Present',
      achievements: [
        'Led development of company\'s main dashboard using Vue.js and TypeScript',
        'Improved application performance by 40% through code optimization',
        'Mentored 3 junior developers and established coding standards',
        'Implemented comprehensive testing strategy reducing bugs by 60%',
        'Collaborated with UX team to redesign user interface increasing user satisfaction'
      ],
      technologies: ['Vue.js', 'TypeScript', 'Node.js', 'Docker', 'AWS'],
      type: 'Full-time',
      location: 'San Francisco, CA',
      icon: '💻',
      dateModified: '2024-01-15',
      duration: '1.5 years',
      size: '1.5 years'
    },
    {
      id: '2',
      role: 'Full Stack Developer',
      company: 'StartupXYZ',
      dates: '2021-06 - 2022-12',
      achievements: [
        'Built entire e-commerce platform from scratch serving 10k+ users',
        'Integrated payment systems and inventory management',
        'Developed RESTful APIs handling 1M+ requests daily',
        'Implemented automated deployment pipeline reducing deployment time by 80%',
        'Created admin dashboard for business analytics and reporting'
      ],
      technologies: ['React', 'Node.js', 'PostgreSQL', 'Redis', 'Stripe'],
      type: 'Full-time',
      location: 'Remote',
      icon: '🚀',
      dateModified: '2023-01-10',
      duration: '1.5 years',
      size: '1.5 years'
    },
    {
      id: '3',
      role: 'Frontend Developer',
      company: 'Digital Agency Pro',
      dates: '2020-03 - 2021-05',
      achievements: [
        'Developed responsive websites for 15+ clients across various industries',
        'Implemented modern UI/UX designs with focus on accessibility',
        'Optimized websites for SEO resulting in 200% increase in organic traffic',
        'Created reusable component library used across multiple projects',
        'Collaborated with designers to ensure pixel-perfect implementations'
      ],
      technologies: ['JavaScript', 'React', 'SCSS', 'Webpack', 'Git'],
      type: 'Full-time',
      location: 'New York, NY',
      icon: '🎨',
      dateModified: '2021-06-01',
      duration: '1.2 years',
      size: '1.2 years'
    },
    {
      id: '4',
      role: 'Junior Web Developer',
      company: 'Local Web Studio',
      dates: '2019-01 - 2020-02',
      achievements: [
        'Learned modern web development practices and industry standards',
        'Contributed to 8+ client projects with HTML, CSS, and JavaScript',
        'Implemented responsive designs for mobile and desktop platforms',
        'Assisted senior developers with debugging and code reviews',
        'Gained experience with version control and agile development processes'
      ],
      technologies: ['HTML', 'CSS', 'JavaScript', 'jQuery', 'Bootstrap'],
      type: 'Full-time',
      location: 'Austin, TX',
      icon: '🌱',
      dateModified: '2020-03-01',
      duration: '1.1 years',
      size: '1.1 years'
    },
    {
      id: '5',
      role: 'Freelance Web Developer',
      company: 'Self-Employed',
      dates: '2018-06 - 2018-12',
      achievements: [
        'Completed 12+ freelance projects for small businesses and individuals',
        'Built custom WordPress themes and plugins',
        'Provided ongoing maintenance and support for client websites',
        'Managed project timelines and client communications independently',
        'Developed strong problem-solving skills working with diverse requirements'
      ],
      technologies: ['WordPress', 'PHP', 'MySQL', 'HTML', 'CSS'],
      type: 'Freelance',
      location: 'Remote',
      icon: '💼',
      dateModified: '2019-01-01',
      duration: '6 months',
      size: '6 months'
    }
  ]
});

// Component state
const selectedExperience = ref<Experience | null>(null);
const openExperiences = ref<Experience[]>([]);
const activeExperienceId = ref<string | null>(null);
const viewMode = ref<'list' | 'icons'>('list');
const sortBy = ref<'role' | 'company' | 'date' | 'duration' | 'type'>('date');
const sortOrder = ref<'asc' | 'desc'>('desc');
const searchQuery = ref('');

// Computed properties
const filteredExperiences = computed(() => {
  let filtered = props.experiences.filter(
      (experience) =>
          experience.role.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
          experience.company.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
          experience.location.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
          (experience.technologies && experience.technologies.some((tech) =>
              tech.toLowerCase().includes(searchQuery.value.toLowerCase())
          ))
  );

  // Sort experiences
  filtered.sort((a, b) => {
    let aValue: any, bValue: any;

    switch (sortBy.value) {
      case 'role':
        aValue = a.role.toLowerCase();
        bValue = b.role.toLowerCase();
        break;
      case 'company':
        aValue = a.company.toLowerCase();
        bValue = b.company.toLowerCase();
        break;
      case 'date':
        aValue = new Date(a.dateModified);
        bValue = new Date(b.dateModified);
        break;
      case 'duration':
        aValue = parseFloat(a.duration);
        bValue = parseFloat(b.duration);
        break;
      case 'type':
        aValue = a.type;
        bValue = b.type;
        break;
      default:
        return 0;
    }

    if (aValue < bValue) return sortOrder.value === 'asc' ? -1 : 1;
    if (aValue > bValue) return sortOrder.value === 'asc' ? 1 : -1;
    return 0;
  });

  return filtered;
});

// Methods
const selectExperience = (experience: Experience) => {
  selectedExperience.value = experience;
};

const openExperience = (experience: Experience) => {
  // Check if experience is already open
  const existingExperience = openExperiences.value.find((e) => e.id === experience.id);
  if (!existingExperience) {
    openExperiences.value.push(experience);
  }
  activeExperienceId.value = experience.id;
};

const closeExperience = (experienceId: string) => {
  const index = openExperiences.value.findIndex((e) => e.id === experienceId);
  if (index > -1) {
    openExperiences.value.splice(index, 1);

    // If closing active experience, switch to another or close all
    if (activeExperienceId.value === experienceId) {
      if (openExperiences.value.length > 0) {
        activeExperienceId.value = openExperiences.value[openExperiences.value.length - 1].id;
      } else {
        activeExperienceId.value = null;
      }
    }
  }
};

const switchToExperience = (experienceId: string) => {
  activeExperienceId.value = experienceId;
};

const toggleViewMode = () => {
  viewMode.value = viewMode.value === 'list' ? 'icons' : 'list';
};

const changeSortBy = (newSortBy: typeof sortBy.value) => {
  if (sortBy.value === newSortBy) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc';
  } else {
    sortBy.value = newSortBy;
    sortOrder.value = sortBy.value === 'date' ? 'desc' : 'asc';
  }
};

const getExperienceIcon = (experience: Experience) => {
  return experience.icon || '💼';
};

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  });
};

const getCurrentTime = () => {
  return new Date().toLocaleTimeString('en-US', {
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  });
};

// const getTotalExperience = () => {
//   return props.experiences.length;
// };

// const getExperienceTypeColor = (type: string) => {
//   const colors = {
//     'Full-time': 'bg-green-100 text-green-800',
//     'Part-time': 'bg-blue-100 text-blue-800',
//     'Contract': 'bg-purple-100 text-purple-800',
//     'Freelance': 'bg-orange-100 text-orange-800',
//     'Internship': 'bg-yellow-100 text-yellow-800'
//   };
//   return colors[type as keyof typeof colors] || 'bg-gray-100 text-gray-800';
// };

const currentTime = ref(getCurrentTime());
setInterval(() => {
  currentTime.value = getCurrentTime();
}, 1000);
</script>

<template>
  <div class="h-full flex flex-col relative">
    <!-- Main Explorer Window -->
    <div class="xp-window m-2 flex-1 flex flex-col" :class="{ 'z-10': !activeExperienceId }">
      <!-- Title Bar -->
      <div class="xp-title-bar">
        <div class="flex items-center">
          <span class="mr-2">💼</span>
          <span class="font-xp-title">My Experience - Career Explorer</span>
        </div>
        <div class="xp-window-controls">
          <div class="xp-control-btn">_</div>
          <div class="xp-control-btn">□</div>
          <div class="xp-control-btn xp-close-btn" @click="toggleOpen">×</div>
        </div>
      </div>

      <!-- XP Menu Bar -->
      <div class="xp-menubar">
        <span class="xp-menu-item inline-block">File</span>
        <span class="xp-menu-item inline-block">Edit</span>
        <span class="xp-menu-item inline-block">View</span>
        <span class="xp-menu-item inline-block">Navigate</span>
        <span class="xp-menu-item inline-block">Help</span>
      </div>

      <!-- Toolbar -->
      <div class="xp-panel p-2 flex items-center justify-between border-b border-gray-400">
        <div class="flex items-center space-x-2">
          <button class="xp-button px-2 py-1 font-xp text-xs">Back</button>
          <button class="xp-button px-2 py-1 font-xp text-xs">Forward</button>
          <button class="xp-button px-2 py-1 font-xp text-xs">Up</button>
          <div class="border-l border-gray-500 h-4 mx-2"></div>
          <button @click="toggleViewMode" class="xp-button px-2 py-1 font-xp text-xs">
            {{ viewMode === 'list' ? 'Icons' : 'List' }}
          </button>
        </div>
        <div class="flex items-center space-x-2">
          <span class="font-xp text-xs">Search:</span>
          <input
              v-model="searchQuery"
              class="xp-input w-32 h-6 text-xs"
              placeholder="Find experience..."
          />
        </div>
      </div>

      <!-- Address Bar -->
      <div class="xp-panel-raised p-1 flex items-center space-x-2">
        <span class="font-xp text-xs">Address:</span>
        <div class="xp-input flex-1 h-6 flex items-center px-2">
          <span class="font-xp text-xs">💼 My Computer > Career > Work Experience</span>
        </div>
      </div>

      <!-- Main Content Area -->
      <div class="flex-1 flex">
        <!-- Left Sidebar -->
        <div class="w-48 border-r-2 border-gray-400 bg-xp-silver">
          <div class="xp-panel-raised m-2 p-2">
            <div class="font-xp text-xs font-bold mb-2">Experience Types</div>
            <div class="space-y-1">
              <div class="font-xp text-xs p-1 hover:bg-blue-100 cursor-pointer">💼 Full-time</div>
              <div class="font-xp text-xs p-1 hover:bg-blue-100 cursor-pointer">⏰ Part-time</div>
              <div class="font-xp text-xs p-1 hover:bg-blue-100 cursor-pointer">📋 Contract</div>
              <div class="font-xp text-xs p-1 hover:bg-blue-100 cursor-pointer">🏠 Freelance</div>
              <div class="font-xp text-xs p-1 hover:bg-blue-100 cursor-pointer">🎓 Internship</div>
            </div>
          </div>

<!--          <div class="xp-panel-raised m-2 p-2">-->
<!--            <div class="font-xp text-xs font-bold mb-2">Career Stats</div>-->
<!--            <div class="space-y-1">-->
<!--              <div class="font-xp text-xs">Total: {{ getTotalExperience() }}</div>-->
<!--              <div class="font-xp text-xs">Years: 5+</div>-->
<!--            </div>-->
<!--          </div>-->

          <div class="xp-panel-raised m-2 p-2">
            <div class="font-xp text-xs font-bold mb-2">Quick Actions</div>
            <div class="space-y-1">
              <button class="w-full xp-button p-1 font-xp text-xs">Export Resume</button>
              <button class="w-full xp-button p-1 font-xp text-xs">Print</button>
              <button class="w-full xp-button p-1 font-xp text-xs">Email</button>
            </div>
          </div>
        </div>

        <!-- Experience List/Grid -->
        <div class="flex-1 p-2 bg-white xp-scroll overflow-auto">
          <!-- List View Header -->
          <div
              v-if="viewMode === 'list'"
              class="flex font-xp text-xs font-bold border-b border-gray-300 pb-1 mb-2"
          >
            <div class="flex-1 cursor-pointer hover:bg-gray-100 p-1" @click="changeSortBy('role')">
              Role {{ sortBy === 'role' ? (sortOrder === 'asc' ? '↑' : '↓') : '' }}
            </div>
            <div class="w-32 cursor-pointer hover:bg-gray-100 p-1" @click="changeSortBy('company')">
              Company {{ sortBy === 'company' ? (sortOrder === 'asc' ? '↑' : '↓') : '' }}
            </div>
            <div class="w-24 cursor-pointer hover:bg-gray-100 p-1" @click="changeSortBy('type')">
              Type {{ sortBy === 'type' ? (sortOrder === 'asc' ? '↑' : '↓') : '' }}
            </div>
            <div class="w-24 cursor-pointer hover:bg-gray-100 p-1" @click="changeSortBy('duration')">
              Duration {{ sortBy === 'duration' ? (sortOrder === 'asc' ? '↑' : '↓') : '' }}
            </div>
            <div class="w-32 cursor-pointer hover:bg-gray-100 p-1" @click="changeSortBy('date')">
              Modified {{ sortBy === 'date' ? (sortOrder === 'asc' ? '↑' : '↓') : '' }}
            </div>
          </div>

          <!-- List View -->
          <div v-if="viewMode === 'list'" class="space-y-1">
            <div
                v-for="experience in filteredExperiences"
                :key="experience.id"
                class="flex items-center p-1 hover:bg-blue-100 cursor-pointer font-xp text-xs"
                :class="{ 'bg-blue-200': openExperiences.includes(experience) }"
                @click="selectExperience(experience)"
                @dblclick="openExperience(experience)"
            >
              <div class="flex items-center flex-1">
                <span class="mr-2">{{ getExperienceIcon(experience) }}</span>
                <div>
                  <div class="font-bold">{{ experience.role }}</div>
                  <div class="text-gray-600">{{ experience.location }}</div>
                </div>
              </div>
              <div class="w-32">{{ experience.company }}</div>
              <div class="w-24">
                  {{ experience.type }}
              </div>
              <div class="w-24">{{ experience.duration }}</div>
              <div class="w-32">{{ formatDate(experience.dateModified) }}</div>
            </div>
          </div>

          <!-- Icons View -->
          <div v-else class="grid grid-cols-4 gap-4">
            <div
                v-for="experience in filteredExperiences"
                :key="experience.id"
                class="flex flex-col items-center p-2 hover:bg-blue-100 cursor-pointer"
                :class="{ 'bg-blue-200': openExperiences.includes(experience) }"
                @click="selectExperience(experience)"
                @dblclick="openExperience(experience)"
            >
              <div class="text-2xl mb-1">{{ getExperienceIcon(experience) }}</div>
              <div class="font-xp text-xs text-center font-bold">{{ experience.role }}</div>
              <div class="font-xp text-xs text-center text-gray-600">{{ experience.company }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Status Bar -->
      <div class="xp-status flex justify-between items-center">
        <div class="flex items-center space-x-4">
          <span class="font-xp">{{ filteredExperiences.length }} experience(s)</span>
          <span v-if="selectedExperience" class="font-xp">{{ selectedExperience.role }} at {{ selectedExperience.company }} selected</span>
        </div>
        <div class="flex items-center space-x-4">
          <span class="font-xp text-xs">{{ openExperiences.length }} open</span>
          <span class="font-xp text-xs">Ready</span>
        </div>
      </div>
    </div>

    <!-- Experience Card Windows -->
    <div
        v-for="(experience, index) in openExperiences"
        :key="experience.id"
        class="absolute"
        :class="{ 'z-20': openExperiences.includes(experience), 'z-10': activeExperienceId !== experience.id }"
        :style="{
        top: `${-20 + index * 30}px`,
        left: `${200 + index * 30}px`,
        width: '1200px',
        height: '650px',
      }"
    >
      <div>
        <ExperienceItem
            :role="experience.role"
            :company="experience.company"
            :dates="experience.dates"
            :achievements="experience.achievements"
            :isOpen="openExperiences.includes(experience)"
            @update:isOpen="
            (val) => {
              if (val) {
                activeExperienceId = experience.id;
              } else {
                closeExperience(experience.id);
              }
            }
          "
        />
      </div>
    </div>

    <!-- XP Taskbar -->
    <div class="xp-taskbar">
      <button class="xp-start-button">Start</button>

      <!-- Quick Launch -->
      <div class="flex items-center space-x-1 mr-4">
        <div
            class="w-6 h-6 bg-blue-500 rounded-sm flex items-center justify-center text-white text-xs cursor-pointer"
        >
          IE
        </div>
        <div
            class="w-6 h-6 bg-yellow-500 rounded-sm flex items-center justify-center text-white text-xs cursor-pointer"
        >
          💼
        </div>
      </div>

      <!-- Open Experience Tabs -->
      <div class="flex items-center space-x-1 flex-1">
        <div
            v-for="experience in openExperiences"
            :key="experience.id"
            class="xp-button px-3 py-1 font-xp text-xs max-w-40 truncate cursor-pointer"
            :class="{ 'border-inset': activeExperienceId === experience.id }"
            @click="switchToExperience(experience.id)"
        >
          {{ experience.role }} - {{ experience.company }}
        </div>
      </div>

      <!-- System Tray -->
      <div class="flex items-center space-x-2">
        <div class="w-4 h-4 bg-green-500 rounded-sm"></div>
        <div class="w-4 h-4 bg-blue-500 rounded-sm"></div>
        <div class="font-xp text-white text-xs">{{ currentTime }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Custom dragging styles */
.cursor-move {
  cursor: move;
}

/* Ensure proper z-indexing for overlapping windows */
.z-10 {
  z-index: 10;
}

.z-20 {
  z-index: 20;
}

/* Smooth transitions for window switching */
.xp-title-bar {
  transition: opacity 0.2s ease;
}

/* Custom scrollbar for experience list */
.xp-scroll::-webkit-scrollbar {
  width: 17px;
  height: 17px;
}

.xp-scroll::-webkit-scrollbar-track {
  background: var(--xp-silver-dark);
  border: 1px inset var(--xp-silver-dark);
}

.xp-scroll::-webkit-scrollbar-thumb {
  background: linear-gradient(
      180deg,
      var(--xp-silver-light) 0%,
      var(--xp-silver) 50%,
      var(--xp-silver-dark) 100%
  );
  border: 1px outset var(--xp-silver-dark);
  border-radius: 0;
}

/* Experience type badges */
.bg-green-100 { background-color: #dcfce7; }
.text-green-800 { color: #166534; }
.bg-blue-100 { background-color: #dbeafe; }
.text-blue-800 { color: #1e40af; }
.bg-purple-100 { background-color: #f3e8ff; }
.text-purple-800 { color: #6b21a8; }
.bg-orange-100 { background-color: #fed7aa; }
.text-orange-800 { color: #9a3412; }
.bg-yellow-100 { background-color: #fef3c7; }
.text-yellow-800 { color: #92400e; }
.bg-gray-100 { background-color: #f3f4f6; }
.text-gray-800 { color: #1f2937; }
</style>